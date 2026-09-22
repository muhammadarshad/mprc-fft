"""
MPRC N=3 ADI shape-holdout benchmark

Requires:
    Python 3
    torch

Frozen N=3 ADI family:
    Lambda = a1+a2+a3
    d1     = a1-a2
    d2     = d1+3
    a1     = (Lambda + 2*d1 + 3)/3
    a2     = (Lambda - d1 + 3)/3
    a3     = (Lambda - d1 - 6)/3

Output/volume invariant:
    O = a1*a2*a3
      = ((Lambda+2d+3)(Lambda-d+3)(Lambda-d-6))/27

The benchmark withholds one complete ADI-family shape for each output class.
MPRC recovers the output structurally from ADI.
GD baselines must learn the output class from examples.
"""

from collections import defaultdict, Counter
import json
import random
import statistics

import torch
import torch.nn as nn
import torch.optim as optim


def adi3_encode(a1, a2, a3):
    if a2 - a3 != 3:
        raise ValueError("N=3 ADI family requires a2-a3 == 3")
    return a1 + a2 + a3, a1 - a2


def adi3_decode(L, d):
    n = L + 2*d + 3
    if n % 3:
        raise ValueError("non-integral ADI state")
    a1 = n // 3
    a2 = a1 - d
    a3 = a1 - (d + 3)
    return a1, a2, a3


def adi3_output(L, d):
    num = (L + 2*d + 3) * (L - d + 3) * (L - d - 6)
    if num % 27:
        raise ValueError("non-integral volume")
    return num // 27


def enumerate_family(hi=255):
    rows = []
    by_output = defaultdict(list)

    for a3 in range(1, hi - 2):
        a2 = a3 + 3
        for a1 in range(a2, hi + 1):
            L, d = adi3_encode(a1, a2, a3)
            assert adi3_decode(L, d) == (a1, a2, a3)

            O = a1*a2*a3
            assert adi3_output(L, d) == O

            rec = {
                "triple": (a1, a2, a3),
                "ADI": (L, d),
                "output": O,
            }
            rows.append(rec)
            by_output[O].append(rec)

    return rows, by_output


class MLP(nn.Module):
    def __init__(self, in_dim, n_classes):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 96),
            nn.ReLU(),
            nn.Linear(96, 96),
            nn.ReLU(),
            nn.Linear(96, n_classes),
        )

    def forward(self, x):
        return self.net(x)


def to_tensor(data, mode):
    X, Y = [], []

    for a1, a2, a3, class_id, _O in data:
        if mode == "raw3":
            feat = [a1/255.0, a2/255.0, a3/255.0]
        elif mode == "adi2":
            L, d = adi3_encode(a1, a2, a3)
            feat = [L/(3*255.0), d/255.0]
        else:
            raise ValueError(mode)

        X.append(feat)
        Y.append(class_id)

    return (
        torch.tensor(X, dtype=torch.float32),
        torch.tensor(Y, dtype=torch.long),
    )


def train_gd(train, test, n_classes, mode, seed, epochs=4000, lr=0.008):
    torch.manual_seed(seed)
    random.seed(seed)

    Xtr, Ytr = to_tensor(train, mode)
    Xte, Yte = to_tensor(test, mode)

    model = MLP(Xtr.shape[1], n_classes)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()

    for _ in range(epochs):
        optimizer.zero_grad()
        loss = loss_fn(model(Xtr), Ytr)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        train_acc = (model(Xtr).argmax(1) == Ytr).float().mean().item()
        test_acc = (model(Xte).argmax(1) == Yte).float().mean().item()

    return train_acc, test_acc


def main():
    rows, by_output = enumerate_family(255)
    multiplicity = Counter(len(v) for v in by_output.values())

    print("=== EXHAUSTIVE N=3 ADI ===")
    print("triples:", len(rows))
    print("distinct outputs:", len(by_output))
    print("outputs with >1 branch:",
          sum(len(v) > 1 for v in by_output.values()))
    print("max branches:", max(map(len, by_output.values())))
    print("multiplicity:", dict(sorted(multiplicity.items())))

    print("\n=== O=19800 ===")
    for rec in by_output[19800]:
        print(rec)

    eligible = [(O, v) for O, v in by_output.items() if len(v) >= 3]
    eligible = sorted(eligible, key=lambda kv: (-len(kv[1]), kv[0]))[:30]
    eligible = sorted(eligible, key=lambda kv: kv[0])

    train, test = [], []

    for class_id, (O, branches) in enumerate(eligible):
        held = branches[-1]

        for rec in branches[:-1]:
            a1, a2, a3 = rec["triple"]
            train.append((a1, a2, a3, class_id, O))

        a1, a2, a3 = held["triple"]
        test.append((a1, a2, a3, class_id, O))

    output_to_class = {
        O: class_id for class_id, (O, _) in enumerate(eligible)
    }

    correct = 0
    traces = []

    for a1, a2, a3, class_id, O in test:
        L, d = adi3_encode(a1, a2, a3)
        recovered = adi3_output(L, d)
        pred = output_to_class.get(recovered)
        ok = pred == class_id
        correct += int(ok)
        traces.append({
            "triple": [a1, a2, a3],
            "ADI": [L, d],
            "expected": O,
            "recovered": recovered,
            "correct": ok,
        })

    mprc_acc = correct / len(test)

    print("\n=== BLIND SHAPE HOLDOUT ===")
    print("classes:", len(eligible))
    print("training branches:", len(train))
    print("held-out branches:", len(test))
    print("MPRC:", mprc_acc)

    results = {}
    for mode in ("raw3", "adi2"):
        runs = [
            train_gd(train, test, len(eligible), mode, seed)
            for seed in (1, 2, 3, 4, 5)
        ]
        results[mode] = runs

        print("\nGD", mode)
        for r in runs:
            print(r)
        print(
            "mean:",
            statistics.mean(r[0] for r in runs),
            statistics.mean(r[1] for r in runs),
        )

    summary = {
        "exhaustive": {
            "triples": len(rows),
            "distinct_outputs": len(by_output),
            "outputs_with_multiple_branches":
                sum(len(v) > 1 for v in by_output.values()),
            "max_branches": max(map(len, by_output.values())),
            "multiplicity": dict(sorted(multiplicity.items())),
        },
        "O_19800": by_output[19800],
        "benchmark": {
            "classes": [O for O, _ in eligible],
            "training_branches": len(train),
            "held_out_branches": len(test),
            "mprc_accuracy": mprc_acc,
            "gd": results,
        },
        "traces": traces,
    }

    Path("mprc_adi_n3_results.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
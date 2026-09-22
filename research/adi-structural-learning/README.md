# ADI Structural Learning Experiments

This folder records the current evidence trail for MPRC observation-populated learning, Arshad's Transpose / ADI structure, and the W²/B¹ freeze.

## Current freeze

- Learned relation: `W^(2) = (x,y) in Z_256^2`, an order-2 relation space of `256^2 = 65,536` states.
- Derived bias: `B^(1) = Delta(W) = x-y mod 256`, an order-1 space of 256 states.
- Derived accumulation: `Sigma(W) = x+y mod 256`.
- `(Sigma, Delta)` is exactly 2-to-1 on `Z_256^2`; the collision partner is `(x+128,y+128)`. One half-turn bit restores bijective recovery.
- Training populates evidence/occupancy attached to `W^(2)` relations; `Sigma` and `B` are not gradient-tuned free scalars.

## Empirical handwritten-digit result

Dataset: scikit-learn `load_digits`, 1,797 real handwritten 8x8 digit images, fixed stratified train/test split (1,257 / 540).

Feature path used in the current empirical run:

`image -> LoG -> Z256 -> local W^(2) relations -> derived Delta/Sigma LUT evidence -> integer class evidence`

No Euclidean distance, cosine similarity, Softmax, or gradient training is used on the MPRC side.

Best current MPRC configuration:

- local horizontal/vertical relations + 64 stride-7 relations
- `W^(2) + B^(1)` integer evidence
- test accuracy: **83.89%**

Controls on the same split:

- logistic regression on float LoG: **96.67%**
- logistic regression on numeric Z256 values: **96.48%**

This does **not** establish superiority over gradient descent. It establishes that an observation-populated deterministic relation LUT is empirically learnable and that the order-1 differential carries substantial reusable discriminative information on real data.

## Next experiment

The remaining vision gap should be attacked with the actual Arshad's ViT structure rather than arbitrary extra tuning:

- local `3x3 = 1 + 8` ADI-9 descriptors
- generator-7 transport
- `16x7 <-> 7x16` orientation transport
- BIND -> REACT -> MEASURE
- learned reaction/prototype LUT policy

The separate QH4 VOF paper is retained as a distinct physics/geometry result; it should not be conflated with the ViT frequency-band feature path.

## Files

- `benchmarks/mprc_adi_n3_benchmark.py` - N=3 ADI shape-holdout benchmark.
- `results/mprc_adi_n3_results.json` - N=3 recorded results.
- `benchmarks/mprc_frozen_W2_B1_test.py` - exhaustive W²/B¹ ring test.
- `results/mprc_frozen_W2_B1_test.json` - exhaustive ring results.
- `results/mprc_digits_empirical_results.json` - first real handwritten-digit benchmark.
- `results/mprc_digits_empirical_evidence_activation.json` - full integer evidence activation ablation.
- `results/mprc_digits_stride7_results.json` - stride-7 relation ablation.
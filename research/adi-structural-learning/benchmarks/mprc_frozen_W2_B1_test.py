from collections import Counter, defaultdict
TAU=256
def add256(a,b): return (a+b)&255
def sub256(a,b): return (a-b)&255
def T(x,y): return add256(x,y),sub256(x,y)
def phase(x,y): return (x>>7)&1

pairs=[(x,y) for x in range(256) for y in range(256)]

# W is order-2: full pair-relation space.
assert len(pairs)==256**2

# B is order-1: delta has 256 states, each representing 256 W-relations.
bc=Counter(sub256(x,y) for x,y in pairs)
assert len(bc)==256
assert set(bc.values())=={256}

# Ring Transpose coordinates alone have a 2-element kernel.
fib=defaultdict(list)
for x,y in pairs:
    fib[T(x,y)].append((x,y))
assert len(fib)==32768
assert set(map(len,fib.values()))=={2}

# Collision partner is exactly simultaneous half-turn.
for pre in fib.values():
    a,b=pre
    assert (((b[0]-a[0])&255),((b[1]-a[1])&255))==(128,128)

# One companion phase bit restores all 65536 states.
seen={}
for x,y in pairs:
    key=(*T(x,y),phase(x,y))
    assert key not in seen
    seen[key]=(x,y)
assert len(seen)==65536

# Core identity remains exact modulo 256.
for x,y in pairs:
    S,D=T(x,y)
    assert ((S*S-D*D)&255)==((4*x*y)&255)

print("PASS")
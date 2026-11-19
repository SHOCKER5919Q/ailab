import math

def ab(d, i, mx, a, b):
    if d == 0: return V[i]
    best = -math.inf if mx else math.inf
    for k in (0, 1):
        v = ab(d-1, 2*i+k, not mx, a, b)
        best = max(best, v) if mx else min(best, v)
        a, b = (max(a, best), b) if mx else (a, min(b, best))
        if b <= a:
            k or print(f"Pruned: node {2*i+1} at depth {d-1}  (alpha={a}, beta={b})")
            break
    return best

V = list(map(int, input("Enter leaf values: ").split()))
print("Optimal value:", ab(int(math.log2(len(V))), 0, True, -math.inf, math.inf))

# SAMPLE OUTPUT
# Enter leaf values: 3 5 6 9 1 2 0 -1
# Pruned: node 3 at depth 0  (alpha=6, beta=5)
# Pruned: node 3 at depth 1  (alpha=5, beta=2)
# Optimal value: 5

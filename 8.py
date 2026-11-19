N = int(input("Enter board size (N): "))

def solve(b):
    if len(b) == N: yield b; return
    for c in range(N):
        if all(c != q and abs(len(b)-i) != abs(c-q) for i, q in enumerate(b)):
            yield from solve(b + [c])

s = next(solve([]), None)
if s:
    print("Positions:", s, "\n")
    for r in s: print(*('Q' if c == r else '.' for c in range(N)))
    print("\nTotal solutions:", sum(1 for _ in solve([])))
else: print("No solution")

# SAMPLE OUTPUT
# Enter board size (N): 8
# Positions: [0, 4, 7, 5, 2, 6, 1, 3]
#
# Q . . . . . . .
# . . . . Q . . .
# . . . . . . . Q
# . . . . . Q . .
# . . Q . . . . .
# . . . . . . Q .
# . Q . . . . . .
# . . . Q . . . .
#
# Total solutions: 92

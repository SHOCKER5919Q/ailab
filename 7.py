import heapq

s = tuple(map(int, input("Enter start state row-wise (0 = blank): ").split()))
G = (1, 2, 3, 4, 5, 6, 7, 8, 0)
h = lambda b: sum(abs(i//3-(v-1)//3) + abs(i%3-(v-1)%3) for i, v in enumerate(b) if v)

if sum(x > y for i, x in enumerate(s) if x for y in s[i+1:] if y) % 2:
    print("Not solvable"); exit()

Q, seen, path = [(h(s), 0, s, [s])], set(), None
while Q:
    f, g, b, p = heapq.heappop(Q)
    if b == G: path = p; break
    if b in seen: continue
    seen.add(b); i = b.index(0)
    for j in (i-3, i+3, i-1, i+1):
        if 0 <= j < 9 and not (i % 3 == 2 and j == i+1) and not (i % 3 == 0 and j == i-1):
            n = list(b); n[i], n[j] = n[j], n[i]; n = tuple(n)
            heapq.heappush(Q, (g+1+h(n), g+1, n, p+[n]))

for k, b in enumerate(path):
    print("Step", k); [print(*('_' if v == 0 else v for v in b[r:r+3])) for r in (0, 3, 6)]
print("Solved in", len(path)-1, "moves")

# SAMPLE OUTPUT
# Enter start state row-wise (0 = blank): 4 1 3 0 2 6 7 5 8
# Step 0     Step 1     Step 2     Step 3     Step 4     Step 5
# 4 1 3      _ 1 3      1 _ 3      1 2 3      1 2 3      1 2 3
# _ 2 6      4 2 6      4 2 6      4 _ 6      4 5 6      4 5 6
# 7 5 8      7 5 8      7 5 8      7 5 8      7 _ 8      7 8 _
# Solved in 5 moves

from collections import deque

a, b, t = map(int, input("Enter jug1, jug2, target: ").split())

def nxt(x, y):
    p, q = min(x, b-y), min(y, a-x)
    return [((a,y),"Fill jug1"), ((x,b),"Fill jug2"), ((0,y),"Empty jug1"),
            ((x,0),"Empty jug2"), ((x-p,y+p),"Pour 1->2"), ((x+q,y-q),"Pour 2->1")]

Q, seen, path = deque([[((0,0), "Start")]]), {(0,0)}, None
while Q:
    p = Q.popleft()
    if t in p[-1][0]: path = p; break
    for s, m in nxt(*p[-1][0]):
        if s not in seen: seen.add(s); Q.append(p + [(s, m)])

if path:
    for i, (s, m) in enumerate(path): print(i, s, "-", m)
    print("Goal reached in", len(path)-1, "steps")
else: print("No solution")

# SAMPLE OUTPUT
# Enter jug1, jug2, target: 4 3 2
# 0 (0, 0) - Start
# 1 (0, 3) - Fill jug2
# 2 (3, 0) - Pour 2->1
# 3 (3, 3) - Fill jug2
# 4 (4, 2) - Pour 2->1
# Goal reached in 4 steps

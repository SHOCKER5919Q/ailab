from collections import deque

M, C, B = map(int, input("Enter missionaries, cannibals, boat size: ").split())
boat = [(m, c) for m in range(B+1) for c in range(B+1) if 1 <= m+c <= B and (m == 0 or m >= c)]
ok = lambda m, c: (m == 0 or m >= c) and (M-m == 0 or M-m >= C-c)

Q, seen, path = deque([[(M, C, 1)]]), {(M, C, 1)}, None
while Q:
    p = Q.popleft(); m, c, s = p[-1]
    if (m, c, s) == (0, 0, 0): path = p; break
    for dm, dc in boat:
        n, d = (m-dm, c-dc) if s else (m+dm, c+dc)
        if 0 <= n <= M and 0 <= d <= C and ok(n, d) and (n, d, 1-s) not in seen:
            seen.add((n, d, 1-s)); Q.append(p + [(n, d, 1-s)])

if path:
    for i in range(1, len(path)):
        (m, c, s), (n, d, _) = path[i-1], path[i]
        print(f"Trip {i}: send {abs(m-n)}M {abs(c-d)}C {'-->' if s else '<--'}"
              f"   Left({n}M,{d}C)  Right({M-n}M,{C-d}C)")
    print("Solved in", len(path)-1, "trips")
else: print("No solution")

# SAMPLE OUTPUT
# Enter missionaries, cannibals, boat size: 3 3 2
# Trip 1: send 0M 2C -->   Left(3M,1C)  Right(0M,2C)
# Trip 2: send 0M 1C <--   Left(3M,2C)  Right(0M,1C)
# Trip 3: send 0M 2C -->   Left(3M,0C)  Right(0M,3C)
# Trip 4: send 0M 1C <--   Left(3M,1C)  Right(0M,2C)
# Trip 5: send 2M 0C -->   Left(1M,1C)  Right(2M,2C)
# Trip 6: send 1M 1C <--   Left(2M,2C)  Right(1M,1C)
# Trip 7: send 2M 0C -->   Left(0M,2C)  Right(3M,1C)
# Trip 8: send 0M 1C <--   Left(0M,3C)  Right(3M,0C)
# Trip 9: send 0M 2C -->   Left(0M,1C)  Right(3M,2C)
# Trip 10: send 0M 1C <--  Left(0M,2C)  Right(3M,1C)
# Trip 11: send 0M 2C -->  Left(0M,0C)  Right(3M,3C)
# Solved in 11 trips

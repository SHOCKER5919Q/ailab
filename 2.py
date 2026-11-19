import random, itertools
N, P = 8, 100
C = list(itertools.combinations(range(N), 2))
f = lambda b: sum(b[i] != b[j] and abs(i-j) != abs(b[i]-b[j]) for i, j in C)

pop = [[0, 4, 7, 5, 2, 6, 1, 3]] + [random.sample(range(N), N) for _ in range(P-1)]

while max(map(f, pop)) < len(C):
    pop = sorted(pop, key=f, reverse=True)[:P//2]
    for _ in range(P - len(pop)):
        a, b = random.sample(pop, 2); p = random.randint(1, N-1)
        c = a[:p] + b[p:]
        i, j = random.sample(range(N), 2)
        if random.random() < .3: c[i], c[j] = c[j], c[i]
        pop.append(c)

b = max(pop, key=f)
print("Positions:", b, "\n")
for r in b: print(*('Q' if c == r else '.' for c in range(N)))
print("\nFitness score :", f(b))

# SAMPLE OUTPUT
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
# Fitness score : 28

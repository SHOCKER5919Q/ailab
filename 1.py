import random
L, P = 8, 10
pop = [random.choices([0, 1], k=L) for _ in range(P)]

while max(map(sum, pop)) < L:
    pop = sorted(pop, key=sum, reverse=True)[:P//2]
    for _ in range(P - len(pop)):
        a, b = random.sample(pop, 2); p = random.randint(1, L-1)
        c = a[:p] + b[p:]
        c[random.randrange(L)] ^= random.random() < .2
        pop.append(c)
    print(''.join(map(str, pop[0])), sum(pop[0]))

b = max(pop, key=sum)
print("Solution:", ''.join(map(str, b)), " Fitness =", sum(b))

# SAMPLE OUTPUT
# 01101110 5
# 01101111 6
# 10111111 7
# Solution: 11111111  Fitness = 8

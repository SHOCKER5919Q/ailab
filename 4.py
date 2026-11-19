W = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
b = [' '] * 9
win = lambda p: any(all(b[i] == p for i in w) for w in W)
show = lambda: [print(*(b[i] if b[i] != ' ' else i+1 for i in r)) for r in (W[0], W[1], W[2])]

def mm(mx):
    if win('O'): return 1, -1
    if win('X'): return -1, -1
    if ' ' not in b: return 0, -1
    r = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if mx else 'X'
            r.append((mm(not mx)[0], i)); b[i] = ' '
    return (max if mx else min)(r)

while ' ' in b:
    show(); m = int(input("Your move (1-9): ")) - 1
    if b[m] != ' ': print("Taken!"); continue
    b[m] = 'X'
    if win('X') or ' ' not in b: break
    b[mm(True)[1]] = 'O'
    if win('O'): break

show()
print("You win!" if win('X') else "AI wins!" if win('O') else "Draw!")

# SAMPLE OUTPUT
# 1 2 3        Your move (1-9): 5      Your move (1-9): 1      Your move (1-9): 3
# 4 5 6        1 2 3                   X 2 3                   X 2 X
# 7 8 9        4 X 6                   4 X 6                   4 X 6
#              7 8 O                   O 8 O                   O O O
#                                                               AI wins!

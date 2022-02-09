import random as rd

player1 = ['T']
player2 = ['T']

for i in range(99):
    player1.append('H')
    player2.append('H')

W1 = 0
W2 = 0

def winner(lista1, lista2):
    global W1
    global W2
    if lista1[-1] == 'T': W1 += len(lista1)
    elif lista2[-1] == 'T': W2 += len(lista2)

Game1 = 0
Game2 = 0

n = 0

while n < 100:
    Turn1 = []
    Turn2 = []
    while True:
        t = rd.randint(0, 99)
        q = rd.randint(0, 99)
        k = ''
        h = ''
        for i, x in enumerate(player1):
            if t == i: Turn1.append(x)
            if t == i: k = x
        for j, y in enumerate(player2):
            if q == j: Turn2.append(y)
            if q == j: h = y
        if k == 'T': Game1 += 1
        elif h == 'T': Game2 += 1 
        if h == 'T' or k == 'T':
            break
    winner(Turn1, Turn2) 
    n += 1

print("Player 1 has", Game1,"to 100 odds after", W1, "flips.")
print("Player 2 has", Game2,"to 100 odds after", W2, "flips.")
print()
print("""Even so, in theory the game is fair. 
Player 1's winning probability is equal to 99/10000 (1/100 times 99/100); 
whilst Player 2's favorable events account for 99/10000 (99/100 times 1/100) each flip.""")
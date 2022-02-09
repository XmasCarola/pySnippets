#calcolo della probabilità di accedere ad una determinata casella partendo dal centro e muovendosi in quattro direzioni

n = 4 #number of steps
m=n*2 +1 +2 #enable steps in all directions plus one spare (m = 11)
b=[[0]*(m) for row in range(m)]
b[n+1][n+1]=1 #set value of start cell to 1

for x in range(n):
    c=[[0]*(m) for row in range(m)]
    for i in range(1, m-1):
        for j in range(1, m-1):
            if b[i][j]>0: #if it is in one cell then it can move to all neighbor cells
                c[i-1][j]+=b[i][j]
                c[i+1][j]+=b[i][j]
                c[i][j-1]+=b[i][j]
                c[i][j+1]+=b[i][j]
    b=c

out=[]
for i in range(m-2):
    out.append('')

for i in range(1, m-1):
    for j in range(1, m-1):
        if b[i][j]>0:
            out[i-1]+=('%3s' % b[i][j])
        else:
            out[i-1]+=('%3s' % ' ')

print('Number of ways to get to a spot:\n')
for i in range(m-2):
    print(out[i])
    
#retrieve data from table

sr = b[n-1][n+1] + sum((b[n][i]) for i in range(n, n+3)) + b[n+1][n+1]
print('\nRed:', sr)
sb = sum((b[n+1][i]) for i in range(n-1, n+4)) - b[n+1][n+1] + sum((b[n+2][i]) for i in range(n, n+3)) + b[n+3][n+1]
print('Blue:', sb)
sy = sum([sum(x) for x in zip(*b)]) - sr - sb
print('Orange:', sy)
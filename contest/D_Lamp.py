import sys
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

h, w = na()
s = nsn(h)

l = [[0] * w for _ in range(h)]
r = [[0] * w for _ in range(h)]
u = [[0] * w for _ in range(h)]
d = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            l[i][j] = 0
            u[i][j] = 0
        else:
            if j == 0:
                l[i][j] = 1
            else:
                l[i][j] = l[i][j - 1] + 1
            
            if i == 0:
                u[i][j] = 1
            else:
                u[i][j] = u[i - 1][j] + 1

for i in range(h - 1, -1, -1):
    for j in range(w - 1, -1, -1):
        if s[i][j] == '#':
            r[i][j] = 0
            d[i][j] = 0
        else:
            if j == w - 1:
                r[i][j] = 1
            else:
                r[i][j] = r[i][j + 1] + 1
            
            if i == h - 1:
                d[i][j] = 1
            else:
                d[i][j] = d[i + 1][j] + 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, l[i][j] + r[i][j] + u[i][j] + d[i][j] - 3)

print(ans)
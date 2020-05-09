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

def sol(a, b):
    b += 1
    s_a = str(a)
    s_b = str(b)
    len_a = len(s_a)
    len_b = len(s_b)
    dp1 = [[0] * 2 for _ in range(len_a + 1)]
    dp2 = [[0] * 2 for _ in range(len_b + 1)]
    for i in range(len_a):
        for j in range(2):
            digmax = 9 if j else int(s_a[i])
            for d in range(digmax + 1):
                ni = i + 1
                nj = j | (d < digmax)
                dp1[ni][nj] += dp1[i][j] + d
    
    for i in range(len_b):
        for j in range(2):
            digmax = 9 if j else int(s_b[i])
            for d in range(digmax + 1):
                ni = i + 1
                nj = j | (d < digmax)
                dp2[ni][nj] += dp2[i][j] + d
    
    print(dp2[len_b][0] - dp1[len_a][0])

while True:
    a, b = na()
    if a == -1:
        break
    sol(a, b)
    
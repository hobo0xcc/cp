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
a = nsn(h)

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[1][1] = 1
for i in range(h):
    for j in range(w):
        if a[i][j] == '.':
            dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]

print(dp[h][w] % mod)
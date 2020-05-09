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

n = ni()
p = nfa()

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1.0
for i in range(n):
    for j in range(i + 1):
        dp[i + 1][j + 1] += dp[i][j] * p[i]
        dp[i + 1][j] += dp[i][j] * (1.0 - p[i])

ans = sum([dp[n][j] for j in range(n // 2 + 1, n + 1)])
print(ans)
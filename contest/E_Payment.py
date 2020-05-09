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

s = ns()
s = "0" + s
n = len(s)

dp = [[0] * 2 for _ in range(n + 1)]
for i in range(n):
    m = int(s[i])
    dp[i + 1][0] = min(dp[i][0], dp[i][1]) + m
    dp[i + 1][1] = min(dp[i][0], dp[i][1])

print(ans)
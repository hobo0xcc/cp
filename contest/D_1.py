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
n = len(s)

dp = [[[0] * 2 for _ in range(11)] for _ in range(n + 1)]
dp[0][0][0] = 1
for i in range(n):
    for j in range(10):
        for k in range(2):
            curdig = int(s[i])
            dmax = 9 if k else curdig
            for dig in range(dmax + 1):
                ni = i + 1
                nj = j + (dig == 1)
                nk = k | (dig < curdig)
                dp[ni][nj][nk] += dp[i][j][k]

ans = 0
for i in range(10):
    ans += i * (dp[n][i][0] + dp[n][i][1])

print(ans)
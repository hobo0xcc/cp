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

d = ni()
n = ns()
lenN = len(n)

dp = [[[0] * 2 for _ in range(d)] for _ in range(lenN + 1)]
dp[0][0][0] = 1
for i in range(lenN):
    for j in range(d):
        for k in range(2):
            curdig = int(n[i])
            dmax = 9 if k else curdig
            for dig in range(dmax + 1):
                ni = i + 1
                nj = (j + dig % d) % d
                nk = k | (dig < curdig)
                dp[ni][nj][nk] += dp[i][j][k]
                dp[ni][nj][nk] %= mod

ans = dp[lenN][0][0] + dp[lenN][0][1] - 1
print(ans % mod)
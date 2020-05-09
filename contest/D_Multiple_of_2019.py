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

dp1 = [[[0] * 2 for _ in range(2)] for _ in range(n + 1)]
dp1[0][0][0] = 1
dp2 = [0] * (n + 1)
dp2[0] = 1
for i in range(n):
    dp2[i + 1] = dp2[i] * 10 % 2019

for i in range(n):
    for j in range(2):
        for k in range(2):
            digmax = 9 if k else int(s[i])
            for dig in range(digmax + 1):
                ni = i + 1
                nj = j | (dig * dp2[n - i - 1] % 2019 == 0)
                nk = k | (dig < digmax)
                dp1[ni][nj][nk] += dp1[i][j][k]

print(dp1[n][1][0] + dp1[n][1][1])
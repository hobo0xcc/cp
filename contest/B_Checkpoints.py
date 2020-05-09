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

n, m = na()
ab = nan(n)
cd = nan(m)

ans = [0] * n
for i in range(n):
    a, b = ab[i]
    cur = inf
    p = -1
    for j in range(m):
        c, d = cd[j]
        dist = abs(a - c) + abs(b - d)
        if dist < cur:
            cur = dist
            p = j + 1
    ans[i] = p

print(*ans, sep="\n")
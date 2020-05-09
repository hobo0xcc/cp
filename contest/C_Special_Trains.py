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

from math import ceil

n = ni()
csf = nan(n - 1)

ans = []
for i in range(n - 1):
    c, s, f = csf[i]
    cur = s + c
    for j in range(i + 1, n - 1):
        nc, ns, nf = csf[j]
        cur = max(ceil(cur / nf) * nf, ns) + nc
    ans.append(cur)
ans.append(0)

print(*ans, sep="\n")
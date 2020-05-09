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
h = na()
ab = nan(m)

g = [[] for _ in range(n)]
for i in range(m):
    a, b = ab[i]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

def ok(v):
    hv = h[v]
    for nv in g[v]:
        if hv <= h[nv]:
            return False
    return True

ans = 0
for i in range(n):
    if ok(i):
        ans += 1

print(ans)
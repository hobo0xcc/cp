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

from collections import deque

n = ni()
a = na()
a.sort()

cur = a[0]
ans = []
for i in range(n - 1, 1, -1):
    ans.append((cur, a[i]))
    if a[i] <= 0:
        cur += a[i]
    else:
        cur -= a[i]
ans.append((a[1], cur))
print(a[1] - cur)
for l, r in ans:
    print(l, r)
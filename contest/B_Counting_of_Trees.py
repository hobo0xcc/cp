import sys

stdin = sys.stdin
inf = 1 << 60
mod = 998244353

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

from collections import defaultdict

n = ni()
d = na()

nxt = -1
d.sort()
if d[0] >= 1:
    print(0)
    exit()

cnt = 1
ans = 1
last = d[0]
for i in range(1, n):
    if d[i] == 0:
        ans = 0
        break
    if abs(d[i] - last) > 1:
        ans = 0
        break
    if last != d[i]:
        ans *= cnt
        cnt = 0
    cnt += 1
    last = d[i]

print(ans)
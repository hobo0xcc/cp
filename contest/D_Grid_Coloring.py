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

h, w = na()
n = ni()
a = na()

ans = [[0] * w for _ in range(h)]
cur = 0
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            ans[i][j] = cur + 1
            a[cur] -= 1
            if a[cur] == 0:
                cur += 1
    else:
        for j in range(w - 1, -1, -1):
            ans[i][j] = cur + 1
            a[cur] -= 1
            if a[cur] == 0:
                cur += 1

for i in range(h):
    print(*ans[i], sep=" ")
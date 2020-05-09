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

n, k = na()
s = ns()

def run_length(a):
    res = [[a[0], 1]]
    last = a[0]
    cnt = 0
    for i in range(1, len(a)):
        if last != a[i]:
            res.append([a[i], 1])
            cnt += 1
        else:
            res[cnt][1] += 1
        last = a[i]
    return res

r = run_length(s)
m = []
for i in range(len(r)):
    if r[i][0] == '1':
        continue
    
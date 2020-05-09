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

n, a, b = na()
s = ns()

cnt = 0
cntb = 0
for i in range(n):
    if s[i] == 'a' and cnt < a + b:
        cnt += 1
        print("Yes")
    elif s[i] == 'b' and cnt < a + b and cntb < b:
        cnt += 1
        cntb += 1
        print("Yes")
    else:
        print("No")
# Author: cr4zjh0bp
# Created: Sun Apr  5 11:47:50 UTC 2020
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

s, l, r = na()


if s > r:
    print(r)
elif s < l:
    print(l)
else:
    print(s)

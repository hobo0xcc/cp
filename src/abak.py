# Author: cr4zjh0bp
# Created: Sun Mar 29 05:26:08 UTC 2020
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

n = ni()
s = ns()

def ok(p):
    k = 0
    for i in range(n):
        if s[i] == p[k]:
            k += 1
        if k == 3:
            return True
    return False

ans = 0
for i in range(1000):
    p = "{:0>3}".format(i)
    if ok(p):
        ans += 1

print(ans)

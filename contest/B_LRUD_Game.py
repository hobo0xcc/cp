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

from collections import Counter

h, w, n = na()
sx, sy = na()
sx -= 1
sy -= 1
s, t = nsn(2)

sc = Counter(s)
tc = Counter(t)

def dropped(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return True
    return False

flag = False
if dropped(max(0, sc['L'] - tc['R']) + sx, sy):
    flag = True
if dropped(sx - max(0, sc['R'] - tc['L']), sy):
    flag = True
if dropped(sx, sy - max(0, sc['U'] - tc['D'])):
    flag = True
if dropped(sx, max(0, sc['D'] - tc['U']) + sy):
    flag = True

print("NO" if flag else "YES")
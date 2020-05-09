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

k = ni()

def bfs():
    q = deque()
    for i in range(1, 10):
        q.append(i)
    cnt = 1
    while len(q):
        p = q.popleft()
        if cnt == k:
            return p
        if p % 10 != 0:
            q.append(p * 10 + (p % 10 - 1))
        q.append(p * 10 + p % 10)
        if p % 10 != 9:
            q.append(p * 10 + (p % 10 + 1))
        cnt += 1

print(bfs())
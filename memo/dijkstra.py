# Author: cr4zjh0bp
# Created: Wed Mar 11 06:00:34 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

from heapq import *

N, M, X, Y = na()
X -= 1
Y -= 1
abw = nan(M)

G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = abw[i]
    a -= 1
    b -= 1
    G[a].append((b, w))

dist = [inf] * N
dist[X] = 0

p = [0 for _ in range(N)]
q = []
heappush(q, (0, X))
while len(q):
    a = heappop(q)[1]
    if p[a]:
        continue
    for i in range(len(G[a])):
        b, w = G[a][i]
        if dist[a] + w < dist[b]:
            dist[b] = dist[a] + w
            heappush(q, (-dist[b], b))

print(dist[Y])

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

from heapq import *

n, m, s = na()
uvab = nan(m)
cd = nan(n)
maxS = 5000

g = [[] for _ in range(n)]
for i in range(m):
    u, v, a, b = uvab[i]
    u -= 1
    v -= 1
    g[u].append((v, (a, b)))
    g[v].append((u, (a, b)))

def dijkstra(g, x):
    dist = [[inf] * (maxS + 7) for _ in range(len(g))]
    dist[x][s] = 0
    q = []
    # proc = [False for _ in range(len(g))]
    heappush(q, (0, (x, s)))
    while len(q):
        p = heappop(q)
        a = p[1][0]
        cost = p[0]
        curs = p[1][1]
        # if proc[a]:
        #	  continue
        # proc[a] = True
        for b in g[a]:
            to = b[0]
            ncost = cost + b[1][1]
            ns = curs - b[1][0]
            if ns >= 0:
                if dist[to][cost] > ncost:
                    heappush(q, (ncost, (to, ns)))
        
        c, d = cd[a]
        cost += d
        curs += c
    
    return dist

# Author: cr4zjh0bp
# Created: Tue Mar 10 11:47:38 UTC 2020
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

# for (int i = 1; i <= n; i++) distance[i] = INF; distance[x] = 0;
# for (int i = 1; i <= n-1; i++) {
#         for (auto e : edges) {
#            int a, b, w;
#            tie(a, b, w) = e;
#            distance[b] = min(distance[b], distance[a]+w);
#         }
# }

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

for i in range(N - 1):
    for j in range(len(G[i])):
        to, w = G[i][j]
        dist[to] = min(dist[to], dist[i] + w)

print(dist[Y])

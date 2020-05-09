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

sys.setrecursionlimit(10 ** 6)

n, m, q = na()
abcd = nan(q)

ans = 0
def dfs(s):
    if len(s) == n + 1:
        res = 0
        for i in range(q):
            a, b, c, d = abcd[i]
            if s[b] - s[a] == c:
                res += d
        return res
    res = 0
    for i in range(s[-1], m + 1):
        news = s[:]
        news.append(i)
        res = max(res, dfs(news))
    return res

print(dfs([1]))
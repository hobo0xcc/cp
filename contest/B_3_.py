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

s = nsn(3)
cnt = [0, 0, 0]
t = 0
while cnt[t] < len(s[t]):
    if s[t][cnt[t]] == 'a':
        cnt[t] += 1
        t = 0
    elif s[t][cnt[t]] == 'b':
        cnt[t] += 1
        t = 1
    else:
        cnt[t] += 1
        t = 2

print(chr(ord('A') + t))
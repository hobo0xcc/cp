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

a, b, c = na()

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and a == b and b == c:
    print(-1)
    exit(0)
ans = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    ta = b // 2 + c // 2
    tb = a // 2 + c // 2
    tc = a // 2 + b // 2
    a, b, c = ta, tb, tc
    ans += 1

print(ans)
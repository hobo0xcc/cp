# Author: cr4zjh0bp
# Created: Sat Mar 14 20:41:10 UTC 2020
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

from collections import Counter

s = ns()
n = len(s)
s = s + "$"
k = ni()

c = []
cnt = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
    elif cnt > 1:
        c.append(cnt)
        cnt = 1

if (len(c) == 1 and c[0] == n) or n == 1:
    print(n * k // 2)
elif s[0] != s[-2]:
    print(sum([x // 2 for x in c[:]]) * k)
else:
    a, b = 1, 1
    if s[0] == s[1]:
        a = c[0]
    if s[-2] == s[-3]:
        b = c[-1]
    print(sum([x // 2 for x in c[:]]) * k - (a // 2 + b // 2 - (a + b) // 2) * (k - 1))

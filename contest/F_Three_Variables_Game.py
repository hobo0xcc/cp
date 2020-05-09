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

n, a, b, c = na()
d = [a, b, c]
s = nsn(n)

ans = []
flag = True
for i in range(n):
    x, y = [ord(c) - ord('A') for c in s[i]]
    if d[x] == 0 and d[y] == 0:
        flag = False
        break
    elif d[x] < d[y]:
        ans.append(x)
        d[x] += 1
        d[y] -= 1
    elif d[x] > d[y]:
        ans.append(y)
        d[x] -= 1
        d[y] += 1
    elif d[x] == d[y] and d[x] >= 2:
        ans.append(x)
        d[x] += 1
        d[y] -= 1
    else:
        if i + 1 == n:
            ans.append(x)
        else:
            nx, ny = [ord(c) - ord('A') for c in s[i + 1]]
            if x == nx:
                ans.append(x)
                d[x] += 1
                d[y] -= 1
            elif y == ny:
                ans.append(y)
                d[x] -= 1
                d[y] += 1
            elif x == 1:
                ans.append(x)
                d[x] += 1
                d[y] -= 1
            else:
                ans.append(y)
                d[x] -= 1
                d[y] += 1

if flag:
    print("Yes")
    for i in range(n):
        print(chr(ans[i] + ord('A')))
else:
    print("No")
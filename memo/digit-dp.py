# Author: cr4zjh0bp
# Created: Sat Feb 29 23:47:46 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

s = ns()
n = len(s)
dp = [[0] * 2 for _ in range(n + 1)]
# dp[i][j]
# i = 左からの桁数
# j = 0; N未満であることが確定していない
# j = 1; N未満であることが確定している
dp[0][0] = 1

for i in range(n):
    for j in range(2):
        D = int(s[i])
        d = 9 if j == 1 else D
        for k in range(d + 1):
            # N未満であることが確定しているならば、1;
            # N未満であることが確定していない場合で、k < D(調べている数がs[i]より小さい)ならば、1
            # それ以外は、0
            dp[i + 1][j or k < D] += dp[i][j]

print(dp[n][0] + dp[n][1])

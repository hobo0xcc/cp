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

class ModInt:
    def __init__(self, n=0, mod=mod):
        self.mod = mod
        self.n = n % self.mod
    
    def value(self):
        return self.n
    
    def __add__(self, rhs):
        if isinstance(rhs, ModInt):
            return self.__class__(self.n + rhs.n, self.mod)
        return self.__class__(self.n + rhs, self.mod)
    
    __radd__ = __add__
    
    def __sub__(self, rhs):
        if isinstance(rhs, ModInt):
            return self.__class__(self.n - rhs.n, self.mod)
        return self.__class__(self.n - rhs, self.mod)
    
    def __rsub__(self, lhs):
        if isinstance(lhs, ModInt):
            return self.__class__(lhs.n - self.n, self.mod)
        return self.__class__(lhs - self.n, self.mod)

    def __mul__(self, rhs):
        if isinstance(rhs, ModInt):
            return self.__class__(self.n * rhs.n, self.mod)
        return self.__class__(self.n * rhs, self.mod)
    
    __rmul__ = __mul__

    def __floordiv__(self, rhs):
        if isinstance(rhs, ModInt):
            return self.__class__(self.n // rhs.n, self.mod)
        return self.__class__(self.n // rhs, self.mod)
    
    def __rfloordiv__(self, lhs):
        if isinstance(lhs, ModInt):
            return self.__class__(lhs.n // self.n, self.mod)
        return self.__class__(lhs // self.n, self.mod)

    def __iadd__(self, rhs):
        if isinstance(rhs, ModInt):
            self.n += rhs.n
        else:
            self.n += rhs
        if self.n >= self.mod:
            self.n -= self.mod
        
        return self
    
    def __isub__(self, rhs):
        rhs_n = rhs.n if isinstance(rhs, ModInt) else rhs
        if self.n < rhs_n:
            self.n += self.mod
        self.n -= rhs_n
        return self
    
    def __imul__(self, rhs):
        rhs_n = rhs.n if isinstance(rhs, ModInt) else rhs
        self.n = self.n * rhs_n % self.mod
        return self
    
    def __ifloordiv__(self, rhs):
        rhs_n = rhs.n if isinstance(rhs, ModInt) else rhs
        exp = self.mod - 2
        while exp:
            if exp % 2:
                self *= rhs_n
            
            rhs_n *= rhs_n
            rhs_n %= self.mod
            exp //= 2
        
        return self
    
    def __pow__(self, exp):
        exp_n = exp.n if isinstance(exp, ModInt) else exp
        if exp_n == 0:
            return self.__class__(1, self.mod)
        if exp_n % 2 == 0:
            t = self.__pow__(exp_n // 2)
            return t * t
        return self * self.__pow__(exp_n - 1)
    
    def __str__(self):
        return str(self.n)

def comb(n, k):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0
    
    res = ModInt(1)
    for i in range(k):
        res *= (n - i)
        res *= ModInt(i + 1) ** (mod - 2)
    
    return res

n, a, b = na()

ans = ModInt(2) ** n - 1
ans -= comb(n, a)
ans -= comb(n, b)
print(ans)
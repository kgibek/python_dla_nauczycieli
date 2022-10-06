#z1
def F(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return F(n-1)-F(n-2)
    
print (F(6))

#z2
def a(n):
    if n==1:
        return 3
    return a(n-1)+3

def b(n):
    if n==1:
        return -2
    return b(n-1)*(-2)

def c(n):
    if n==1:
        return 8
    return c(n-1)/(-2)

def d(n):
    if n==1:
        return 2
    if n==2:
        return 6
    return d(n-2)+1

def e(n):
    if n==1:
        return -1
    if n==2:
        return 4
    return e(n-2)*e(n-1)

def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return -4
    return f(n-3)+f(n-1)

def g(n):
    if n==1:
        return 1.5
    if n==2:
        return 1
    if n==3:
        return 0.5
    return g(n-1)-((g(n-2)-g(n-1))+(g(n-3)-g(n-2)))

#3
def s(n):
    if n==0:
        return 1
    return n*s(n-1)

def dwumian(n,k):
    return s(n)/(s(k)*s(n-k))

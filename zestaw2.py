#Czy podana liczba jest liczbą pierwszą?
import sys
def pierwsza(n):
    d=int(n**(1/2))
    for i in range(2,d+1):
        if n%i==0:
            print(n, " nie jest liczbą pierwszą")
            sys.exit()
    print(n," jest liczbą pierwszą")

# Czy podane dwie liczby są liczbami bliźniaczymi?
def blizniacze(n,m):
    if pierwsza2(n)==1 and pierwsza2(m)==1 and abs(m-n)==2: return print("blizniacze")
    else: return print ("nie są blizniacze")

#Czy podane dwie liczby są liczbami zaprzyjaźnionymi? Znajdź liczby doskonałe w przedziale (6,10001).
    
def suma_dzielnikow(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s

def zaprzyjaznione(n,m):
    if suma_dzielnikow(n)==m or suma_dzielnikow(m)==n:
        return print("TAK")
    return print ("NIE")

def doskonale ():
    for i in range(6,10001):
        if i==suma_dzielnikow(i):
            print (i)
    

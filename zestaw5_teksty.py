#1a
def oblicz(tekst):
    j=tekst.count('d')+tekst.count('D')
    return j

#print(oblicz('daDada'))

#1b
def b(tekst):
    return tekst[::-1]
#print(b('Karolina'))

#1c
def c(tekst):
    j=0
    for k in tekst:
        if k!='a' and k!='A':
            j+=1
    return j
#print(c('Adndj'))

#1d
def d(tekst):
    tekst=list(tekst)
    n=len(tekst)
    for i in range(n):
        if tekst[i]!='b' and tekst[i]!='B':
            tekst[i]='a'
    tekst=''.join(tekst)
    print(tekst)
#d('Brbkjfdjaba')

#1e
def e(tekst):
    w=""
    for k in tekst:
        if k!='s':
            w=w+k
    return w
#print(e('saksaks'))

#1f
def f(tekst):
    j=0
    n=len(tekst)
    for i in range(0,n,3):
        if tekst[i]!='d' and tekst[i]!='D':
            j+=1
    return j
#print(f('Dadaaada'))

#1g
def g(tekst):
    tekst=list(tekst)
    n=len(tekst)
    for i in range(n):
        if tekst[i]=='m' or tekst[i]=='M':
            tekst[i]='R'
    tekst=''.join(tekst)
    return tekst
#print(g("mama"))

#2
def palindrom(tekst):
    tekst=tekst.lower()
    tekst2=tekst[::-1]
    if tekst2==tekst:
        print(tekst, "jest palindromem")
    else:
        print(tekst, "nie jest palindromem")
#palindrom('amam')
#palindrom('kajak')

#3
def zdania(tekst):
    a=tekst.lower()
    a=a.split()
    a=''.join(a)
    tekst2=a[::-1]
    if tekst2==a:
        print(tekst, "jest palindromem")
    else:
        print(tekst, "nie jest malindromem")
#zdania('Ala ma kota')
#zdania('Nogawka jak wagon')
        

    
    


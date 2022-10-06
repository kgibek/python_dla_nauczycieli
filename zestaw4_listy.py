
#obliczenie sumy wszystkich elementów listy
def przyklad1_suma(T):
    n=len(T)
    s=0
    for i in range(n):
        s+=T[i]
    return s

print("przyklad1_suma(lista)= ", przyklad1_suma([3,4,5,5,7,9,4,2,1]))
print("przyklad1_suma(krotka)= ", przyklad1_suma((3,4,5,5,7,9,4,2,1)))

def przyklad1a_suma(T):
    s=0
    for k in T:
        s+=k
    return s
print("przyklad1a_suma(lista)= ", przyklad1a_suma([3,4,5,5,7,9,4,2,1]))
print("przyklad1a_suma(krotka)= ", przyklad1a_suma((3,4,5,5,7,9,4,2,1)))

#obliczanie iloczynu tych elementów listy/krotki, które są mniejsze od 6

def iloczyn(T):
    i=1
    for k in T:
        if k<6:
            i*=k
    return i

print(iloczyn([2,3,5,8]))

#Obliczanie liczby tych elementów listy/krotki, których indeks nie jest podzielny przez 5
def niepodz5(T):
    l=0
    n=len(T)
    for i in range(n):
        if i%5!=0:
            l+=1
    return l

print(niepodz5([1,2,3,5,7,8,9]))

#zadanie 1a - wypisanie elementów listy 
def elementy(T):
    print("elementy listy")
    for k in T:
        print (k)

elementy([2,3,4,5,67])
'''
"""wyzerowanie tych elementów listy, które mają nieparzysty indeks zawarty w przedziale [3,8) i wyświetlenie tej listy"""
'''
def zerowanie(T):
    n=len(T)
    for i in range(n):
        if i>=3 and i<8 and i%2==1:
            T[i]=0
    print(T)

zerowanie([1,3,5,6,7,89,9,5,6,3,6])

def zerow(T):
    for i in range(3,8,2):
        T[i]=0
    return T

#zadanie 1d Sprawdzenie czy na liście znajdują się elementy ujemne

def d(T):
    for k in T:
        if k<0:
            print ("są elementy ujemne")
            return False
    print ("wszystkie elementy są nieujemne")
    return True
    
d([1,2,3,5,7,9])

#sprawdzenie czy na liście/w krotce znjduje się element o wartości różnej od 2
def elemdwa(T):
    for k in T:
        if k!=2:
            print("znajduje się element różny od 2")
            return True
    print ("nie znajduje się element różny od 2")
    return False

elemdwa([2,2,2])


#sprawdzenie czy na liście/w krotce jest element o wartości podanej przez użytkownika
def spr(T,n):
    for k in T:
        if k==n:
            print("znajduje się")
            return True
    print("nie znajduje się")
    return False
    
spr([2,3,5,67,7],7)


#zadanie 2a
def wypisywanie(T,m):
    for i in range(m):
        print (T[i])

#wypisywanie([[2,3,4,5],[7,6,4,5],[8,9,4,5]],3)
        
def wypisywanie2(T):
    for P in T:
        print (P)
#wypisywanie2([[2,3,4,5],[7,6,4,5],[8,9,4,5]])

#obliczenie sumy tych elementów listy, które są niepodzielne przez 3
def niepodz3(T,m,n):
    s=0
    for i in range(m):
        for j in range(n):
            if T[i][j]%3:
                s+=T[i][j]
    return s

#print(niepodz3([[2,34,4,5],[3,6,9,8,7]],2,3))

def niepodz3a(T):
    s=0
    for P in T:
        for k in P:
            if k%3:
                s+=k
    return s

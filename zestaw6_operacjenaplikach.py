#Ćwiczenie 1
dane=open("dane.txt","r")
wynik=open("wyniki_1.txt","w")
for k in dane:
    if len(k.rstrip())%2==0:
        wynik.write(k)
dane.close()
wynik.close()

#Ćwiczenie 2
dane=open("dane_2.txt","r")
wyniki=open("wyniki_2.txt","w")
for k in dane:
    w=int(k)**2
    if w%3==0:
        wyniki.write(str(w)+"\n")
dane.close()
wyniki.close()


#Napisz program wykonujacy nastepujacą operację: wpisanie do pliku tekstowego dane zestaw6 1.txt w kolejnych wierszach nazw miesiecy

#Zad.1
zapis=open("dane_zestaw6_1.txt","w")
zapis.write("Styczeń \nLuty \nMarzec \nKwiecień \nMaj \nCzerwiec \nLipiec \nSierpień \nWrzesień \nPaździernik \nListopad \nGrudzień")
zapis.close()

# importation de la fonction logarithme

from math import log

#initialisation du nombre à convertir sa base d'écriture et sa base de convertion

n=int(input('Nombre à convertir:'))
C=int(input("Base d'écriture:"))
N=int(input('Base de conversion:'))

chiffressup=['A','B','C','D','E','F']
P=[]



def convert(n):
    L=int(log(n)/log(N))
    s=int(n/(N**L))
    A=n
    rpartiel=[str(s)]
    while L>0:
        A-=(N**L)*s
        L-=1
        s=int(A/(N**L))
        rpartiel.append(str(s))

    for i in range(0,len(rpartiel)):
        if int(rpartiel[i])>=10:
            rpartiel[i]=chr(int(rpartiel[i])+87)
    return rpartiel
    
if C<11:
    X=str(n)
    nbdepart=[]
    l=len(X)
    a=-1
    resultat=[]

    while l>0:
        a+=1
        l-=1
        resultat.append(int(X[a])*(C**l))

    for i in range(0,len(X)):
        nbdepart.append(int(X[i]))
    if max(nbdepart)>=C:
        print( "Votre nombre n'est pas en base ",C,'.')
    else:
        print( "Votre nombre en base",N," est :", "".join(convert(sum(resultat))))

elif 11<C<16 :
    resultat=[]
    taille_n=str(n)
    for i in range(0,len(taille_n)):
        P.append(taille_n[i])
    for i in range(0,len(P)):
        if P[i] in chiffressup :
            P[i]=str(ord(P[i])-87)
    if int(max(taille_n))>=C:
        print( "Votre nombre n'est pas en base ",C,'.')
    l=len(P)-1
    a=0
    while l>-1:
        resultat.append(int(P[a])*C**l)
        l-=1
        a+=1
    else :
        print( "Votre nombre en base",N," est :", "".join(convert(sum(resultat))))



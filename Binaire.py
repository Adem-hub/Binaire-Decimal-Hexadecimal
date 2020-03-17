import copy
from copy import deepcopy

#Utilisez ces trois fonctions , elles reprennent ce que les autres font déja.
#Pour l'hexadecimal, il faut mettre un string en argument.

def BinaireToAll(binaire):
    Dec= BinaireToDecimal(binaire)
    Hexa=DecimalToHexa(Dec)
    Tot= "Decimal: "+ str(Dec)+ " \nHexaDecimal: "+ str(Hexa)
    print(Tot+'\n')
    return [Dec,Hexa]

def DecimalToAll(decimal):
    Hexa= DecimalToHexa(decimal)
    Binaire= DecimalToBinaire(decimal)
    Tot= "Binaire: "+ str(Binaire)+ " \nHexaDecimal: "+ str(Hexa)
    print(Tot+'\n')
    return [Binaire,Hexa]

def HexaToAll(hexa):
    Dec= HexaToDecimal(hexa)
    Binaire=DecimalToBinaire(Dec)
    Tot= "Binaire: "+ str(Binaire)+ " \nDecimal: "+ str(Dec)
    print(Tot+'\n')
    return [Binaire,Dec]















def BinaireToDecimal(binaire):
    binaire=deepcopy(binaire)
    Decimal=[]
    facteur=1
    binaire=str(binaire)
    a= reversed(binaire)
    for item in a:
        if item !='1' and item!= '0':
            return "Ce n'est pas du binaire"
        else:
            it=int(item)
            it= it*facteur
            Decimal.append(it)
            facteur*=2
    Total=sum(Decimal)
    return Total

def DecimalToHexa(binaire):
    binaire= deepcopy(binaire)
    binaire= str(binaire)
    hexa=""
    a=int(binaire)%16
    while binaire!=0:
        a=int(binaire)%16

        if a==10:
            hexa= hexa+ "A"
        if a==11:
            hexa= hexa+ "B"
        if a==12:
            hexa= hexa+ "C"
        if a==13:
            hexa= hexa+ "D"
        if a==14:
            hexa= hexa+ "E"
        if a==15:
            hexa= hexa+ "F"
        if a in range(0,10):
            if int(binaire)!=0:
                hexa=hexa+str(a)
        binaire=int(binaire)/16
    hexa= hexa[::-1]
    return hexa

def DecimalToBinaire(decimal):
    decimal= deepcopy(decimal)
    decimal= str(decimal)
    bi=""
    a=int(decimal)%2
    while decimal!=0:
        a=int(decimal)%2
        if int(decimal) !=0:
            bi=bi+str(a)
        decimal=int(decimal)/2
    bi= bi[::-1]
    return bi

def HexaToDecimal(hexa):
    hexa= deepcopy(hexa)
    facteur=1
    L=[]
    hexa= reversed(hexa)
    for item in hexa:
        if item =="A" or item == "a":
            item= 10*facteur
            L.append(item)
        if item =="B" or item == "b":
            item= 11*facteur
            L.append(item)
        if item =="C" or item == "c":
            item= 12*facteur
            L.append(item)
        if item =="D" or item == "d":
            item= 13*facteur
            L.append(item)
        if item =="E" or item == "e":
            item= 14*facteur
            L.append(item)
        if item =="F" or item == "f":
            item= 15*facteur
            L.append(item)
        if int(item) in range(0,10):
            item=int(item)*facteur
            L.append(item)
        facteur=facteur*16

    ka=sum(L)
    return ka















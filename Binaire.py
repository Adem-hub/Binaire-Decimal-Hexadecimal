import copy
from copy import deepcopy
"Entrez un argument qui est un string contenant le binaire, le decimal ou bien l'hexadecimal"
#Le binaire est fini.
#Decimal ....
#HexaDecimal ....

def BinaireToAll(binaire):
    Dec= BinaireToDecimal(binaire)
    Hex=DecimalToHexa(Dec)
    Tot= "Decimal: "+ str(Dec)+ " \nHexaDecimal: "+ str(Hex)
    print(Tot+'\n')
    return [Dec,Hex]

def DecimalToAll():
    a="Work in Progress"
    return a

def HexaToAll():
    a="Work in Progress"
    return a

def BinaireToDecimal(binaire):
    binaire=deepcopy(binaire)
    Decimal=[]
    facteur=1
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
    hexa=""
    a=int(binaire)%16
    while binaire!=0:

        a=int(binaire)%16
        print(a)
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
            hexa=hexa+str(a)

        binaire=int(binaire)/16


    hexa= hexa.replace('0','')
    hexa= hexa[::-1]
    return hexa











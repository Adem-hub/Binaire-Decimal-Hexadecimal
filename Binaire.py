import copy
from copy import deepcopy
"Entrez un string contenant le binaire"
def BinaryToDecimal(binary):
    binary=deepcopy(binary)
    Decimal=[]
    facteur=1
    a= reversed(binary)
    for item in a:
        it=int(item)
        it= it*facteur
        Decimal.append(it)
        facteur*=2
    Total=sum(Decimal)
    return Total









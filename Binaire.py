import copy
from copy import deepcopy

import os
#Utilisez ces trois fonctions , elles reprennent ce que les autres font déja.
#Pour l'hexadecimal, il faut mettre un string en argument.
def dossier():
    os.chdir("C://Users//Ridha//Desktop//binaire")
dossier()
import Calcul as Cl

def BinaireToAll(binaire):
    Dec= Cl.BinaireToDecimal(binaire)
    Hexa=Cl.DecimalToHexa(Dec)
    Tot= "Decimal: "+ str(Dec)+ " \nHexaDecimal: "+ str(Hexa)
    print(Tot+'\n')
    return [Dec,Hexa]

def DecimalToAll(decimal):
    Hexa= Cl.DecimalToHexa(decimal)
    Binaire= Cl.DecimalToBinaire(decimal)
    Tot= "Binaire: "+ str(Binaire)+ " \nHexaDecimal: "+ str(Hexa)
    print(Tot+'\n')
    return [Binaire,Hexa]

def HexaToAll(hexa):
    Dec= Cl.HexaToDecimal(hexa)
    Binaire=Cl.DecimalToBinaire(Dec)
    Tot= "Binaire: "+ str(Binaire)+ " \nDecimal: "+ str(Dec)
    print(Tot+'\n')
    return [Binaire,Dec]






























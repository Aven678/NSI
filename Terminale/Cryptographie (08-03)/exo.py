from math import gcd
from sympy.crypto.crypto import encipher_affine, decipher_shift, decipher_affine
def dechiffre():
    msg = "RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV"
    for k in range(26):
        ct = decipher_shift(msg, k)
        if 'FACILE' in ct:
            print(ct)

def rang(lettre):
    return ord(lettre)-65

def affine(msg, a, b):
    result = ""
    for lettre in msg:
        rg = rang(lettre)
        nv_rg = (a*rg + b)%26
        nv_lettre = chr(nv_rg + 65)
        result += nv_lettre

    return result

def affine_sympy(msg,a,b):
    return encipher_affine(msg,(a,b))

def dechiffre():
    msg = "UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC"
    for a in range(20):
        for b in range(20):
            ct = decipher_affine(msg, gcd(a,b))
            if 'TRAVAIL' in ct:
                print(ct)
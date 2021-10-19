class Cellule:
    def __init__(self, valeur, link):
        self.valeur = valeur
        self.link = link

lst = Cellule(3, Cellule(5, Cellule(1,None)))
print(lst.valeur)
print(lst.link.valeur)
print(lst.link.link.valeur)

def oui(n, lst=Cellule(1,None)):
    if n == 1:
        return lst
    else:
        oui(n-1, Cellule(n, lst))

print(oui(10))
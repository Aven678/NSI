#Ex 1
def delta(tab):
    result = [tab[0]]
    for i in range(1, len(tab)):
        result.append(tab[i]-tab[i-1])
    return result

#Ex 2
class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def est_une_feuille(self):
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ""
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)

    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + str(expression_infixe(e.droit))
    if e.est_une_feuille():
        return s

    return '('+s+')'
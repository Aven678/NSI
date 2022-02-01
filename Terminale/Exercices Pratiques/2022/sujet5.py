#Ex 05.1
def rechercheMinMax(tab):
    dic = {'min': None, 'max':None}
    for i in tab:
        if dic['min'] == None:
            dic['min'] = i

        if dic['max'] == None:
            dic['max'] = i

        if dic['min'] > i:
            dic['min'] = i

        if dic['max'] < i:
            dic['max'] = i

    return dic

#Ex 05.2
class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for nb_coul in range(1,5):
            for val in range(1,14):
                self.contenu.append(Carte(nb_coul, val))

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        #A compléter
        return self.contenu[pos]
        
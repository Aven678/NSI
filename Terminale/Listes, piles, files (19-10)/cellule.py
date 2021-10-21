class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante

class Pile :
    def __init__(self):
        self.data = None

    def est_vide(self):
        return self.data == None

    def empile(self, valeur):
        self.data = Cellule(valeur, self.data)

    def depile(self):
        if self.est_vide():
            raise IndexError("Vous avez essayé de dépiler une pile vide !'")

        contenu = self.data.contenu
        self.data = self.data.suivante
        return contenu

    def __str__(self) -> str:
        text = "|"
        cellule = self.data
        while cellule != None:
            text = text+str(cellule.contenu)+"|"
            cellule = cellule.suivante

        return text

    def __repr__(self) -> str:
        text = "|"
        cellule = self.data
        while cellule != None:
            text = text+str(cellule.contenu)+"|"
            cellule = cellule.suivante

        return text
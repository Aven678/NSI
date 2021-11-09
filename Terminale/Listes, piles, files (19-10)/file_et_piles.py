class Pile:
    def __init__(self) -> None:
        self.data = []

    def est_vide(self):
        return len(self.data) == 0

    def empile(self, element):
        self.data.append(element)
    
    def depile(self):
        if self.est_vide():
            raise IndexError('Vous avez essayé de dépiler une pile vide !')
        return self.data.pop()

class File:
    def __init__(self) -> None:
        self.entree = Pile()
        self.sortie = Pile()

    def enfile(self, x):
        self.entree.empile(x)

    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()

    def defile(self):
        if self.est_vide():
            raise IndexError("c'est non Grrrr")

        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empile(self.entree.depile())

        return self.sortie.depile()
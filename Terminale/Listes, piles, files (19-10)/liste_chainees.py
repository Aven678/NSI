class Cellule:
    def __init__(self, valeur, link):
        self.valeur = valeur
        self.link = link

lst = Cellule(3, Cellule(5, Cellule(1,None)))
 
class Pile:
    def __init__(self) -> None:
        self.data = []

    def est_vide(self):
        return len(self.data) == 0

    def empile(self, element):
        self.data.append(element)
    
    def depile(self):
        if self.est_vide() == True :
            raise IndexError('Vous avez essayé de dépiler une pile vide !')
        return self.data.pop()

    def __str__(self) -> str:
        if len(self.data) == 0:
            return "None"

        text = "|"
        for i in self.data:
            text += str(i)+"|"

        return text

    def __repr__(self) -> str:
        if len(self.data) == 0:
            return "None"

        text = "|"
        for i in self.data:
            text += str(i)+"|"

        return text
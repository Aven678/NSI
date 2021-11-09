class Pile:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return len(self.data) == 0 


    def empile(self,x):
        self.data.append(x)

    def depile(self):
        if self.est_vide() == True :
            raise IndexError('Vous avez essayé de dépiler une pile vide !')
        else :
            return self.data.pop() 

    def __str__(self):       # Hors-Programme : pour afficher 
        s = '|'              # convenablement la pile avec print(p)
        for k in self.data :
            s = s + str(k) + '|'
        return s

    def __repr__(self):       # Hors-Programme : pour afficher 
        s = '|'              # convenablement la pile avec p
        for k in self.data :
            s = s + str(k) + '|'
        return s  

class Nav:
    def __init__(self):
        self.pile = Pile()

    def visite(self, site):
        self.pile.empile(site)
        print("page actuelle :", site)

    def back(self):
        if self.pile.est_vide == True:
            raise IndexError("Vous êtes retourné à la première page")

        page_quittee = self.pile.depile()
        print("page quittée :", page_quittee)
        page_actuelle = self.pile.depile()
        self.pile.empile(page_actuelle)
        print("page actuelle :", page_actuelle)
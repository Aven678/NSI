class TriangleRect:
    def __init__(self,cote1,cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenuse = (self.cote1**2 + self.cote2**2)**0.5
    

class Voiture:
    def __init__(self, annee, coul, vmax) :
        self.annee = annee
        self.couleur = coul
        self.vitesse_max = vmax
        self.age = 2021 - self.annee
        
    def petite_annonce(self):
        """Annonce une vente sur le véhicule"""
        print("A vendre voiture", self.couleur, "de", self.annee, \
              ", vitesse maximale", self.vitesse_max, "km/h.")
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self):
        return (self.x**2+self.y**2)**0.5
    
def distance_point(A,B):
    return ((A.x+B.x)**2+(A.y+B.y)**2)**0.5
    
def test_rectangle(A,B,C):
    distanceAB = distance_point(A,B)
    distanceAC = distance_point(A,C)
    distanceBC = distance_point(B,C)
    
    if (distanceAB == distanceAC**2 +distanceBC**2) or (distanceAC == distanceAB**2 + distanceBC**2) or (distanceBC == distanceAB**2+distanceAC**2):
        return True
    else:
        return False
    
    
class Eleve:
    def __init__(self, nom, classe, note):
        self.nom = nom
        self.classe = classe
        self.note = note
        
        
def compare(eleve1, eleve2):
    note1 = eleve1.note
    note2 = eleve2.note
    
    if (note1 > note2):
        return eleve1.nom
    elif (note2 > note1):
        return eleve2.nom
    else:
        return "Les deux élèves ont la même note"
        
class Chrono:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        
    def affiche(self):
        return "Il est {}h {}m et {}s".format(self.heures, self.minutes, self.secondes)
    
    def avance(self, sec):
        self.secondes += sec
        
        self.minutes += sec // 60 #division euclidienne
        self.secondes = self.secondes % 60 #modulo
        
        self.heures += self.minutes // 60
        self.minutes = self.minutes % 60
        
class Fraction :
    def __init__(self, den, num) :
        self.denominateur = den
        self.numerateur = num

    def __str__(self):
        return str(self.denominateur)+"/"+str(self.numerateur)
        
class Player:
    def __init__(self):
        self.energie = 3
        self.alive = True
        
    def blessure(self):
        if (self.alive):
            self.energie -= 1
            if (self.energie == 0):
                self.alive = False
            
    def bonus(self):
        if (self.alive):
            self.energie += 1
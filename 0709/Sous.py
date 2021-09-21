class Fraction:
    def __init__(self,den,num):
        self.denominateur = den
        self.numerateur = num
        
    def __str__(self):
        if self.numerateur == 1:
            return str(self.denominateur)
        return str(self.denominateur)+"/"+str(self.numerateur)
import pygame, sys
import time
from pygame.locals import *

from random import randint
import numpy as np

longueur,largeur = 1040,980

taille = 20

class Balle:
    def __init__(self, id_balle):
        self.id = id_balle
        
        self.x = randint(5, longueur)
        self.y = randint(5, largeur)
        
        self.dx = randint(-10,10)
        self.dy = randint(-10,10)
        self.couleur = np.random.choice(range(256), size=3)
        self.alive = True
    
    def draw(self):
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),taille)
        
    def avance(self, balles):        
        self.draw()
        
        if self.x < taille or self.x > longueur - taille :
            self.dx = -self.dx
    
        if self.y < taille or self.y > largeur - taille:
            self.dy = -self.dy
        
        self.x += self.dx
        self.y += self.dy
        
        self.collision(balles)
        
    def collision(self, balles):
        for balle in balles:
            if balle.id == self.id:
                continue
            
            if balle.alive == False:
                continue
            if self.distanceAB(balle.x,balle.y) < 2*taille:
                self.dx,balle.dx = balle.dx,self.dx
                self.dy,balle.dy = balle.dy,self.dy
        
    
    def distanceAB(self, xB, yB):
        return ((xB-self.x)**2+(yB-self.y)**2)**0.5



balles = [Balle(x) for x in range(int(input("Tu veux combien de balles ? ")))]
print("Il y a",len(balles)," balles. ALLEZ ZÉ PARTI !")

pygame.display.init()
fenetre = pygame.display.set_mode((longueur, largeur))
fenetre.fill([0,0,0])

while True:
    fenetre.fill([0,0,0])
    
    balle_dead = 0
    
    for balle in balles:
        if balle.alive == False:
            balle_dead += 1
            continue
        balle.avance(balles)
    
    if balle_dead == len(balles):
        print("Et c'est gagné ! Bravo !")
        pygame.display.quit()
        sys.exit()
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            for b in balles:
                if b.alive == False:
                    continue
                if (mouseX >= b.x-taille and mouseX <= b.x+taille) and (mouseY <= b.y+taille and mouseY >= b.y-taille):
                    b.alive = False
        
        if event.type == pygame.QUIT:
            print("Ah c'est la fin... Adieu.")
            pygame.display.quit()
            sys.exit()
            
    time.sleep(0.05)
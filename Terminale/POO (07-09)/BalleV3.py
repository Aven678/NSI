import pygame, sys
import time
from pygame.locals import *

from random import randint
import numpy as np

longueur,largeur = 1040,980

taille = 10

class Balle:
    def __init__(self):
        
        self.x = randint(5, longueur)
        self.y = randint(5, largeur)
        
        self.dx = randint(-10,10)
        self.dy = randint(-10,10)
        self.couleur = np.random.choice(range(230), size=3)
        self.taille = taille
    
    def draw(self):
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.taille)
        
    def avance(self):        
        self.draw()
        
        if self.x < self.taille/2 or self.x > longueur - self.taille/2 :
            self.dx = -self.dx
    
        if self.y < self.taille/2 or self.y > largeur - self.taille/2:
            self.dy = -self.dy
        
        self.x += self.dx
        self.y += self.dy
        
        self.collision()
        
    def collision(self):
        for balle in balles:
            if balle == self:
                continue
        
            if self.distanceAB(balle.x,balle.y) < self.taille:
                self.taille += 0.2
                balles.remove(balle)
        
    
    def distanceAB(self, xB, yB):
        return ((xB-self.x)**2+(yB-self.y)**2)**0.5

balles = [Balle() for x in range(500)]
print("Il y a",len(balles)," balles à manger. ALLEZ ZÉ PARTI !")

pygame.display.init()
fenetre = pygame.display.set_mode((longueur, largeur))
fenetre.fill([0,0,0])


main_balle = Balle()
main_balle.couleur = (255,0,0)
main_balle.x = longueur/2
main_balle.y = largeur/2
main_balle.taille = 15
main_balle.dx = 0
main_balle.dy = 0

def arret():
    print("Fin du jeu, merci d'avoir joué")
    pygame.display.quit()
    sys.exit()

while True:
    fenetre.fill([255,255,255])

    if main_balle.taille >= longueur:
        arret()

    for balle in balles:
        balle.draw()

    main_balle.draw()
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                if main_balle.dx <= 0:
                    main_balle.dx = 5
                    main_balle.dy = 0

            elif event.key == K_UP or event.key == K_z:
                if main_balle.dy >= 0:
                    main_balle.dy = -5
                    main_balle.dx = 0

            elif event.key == K_LEFT or event.key == K_q:
                if main_balle.dx >= 0:
                    main_balle.dx = -5
                    main_balle.dy = 0

            elif event.key == K_DOWN or event.key == K_s:
                if main_balle.dy <= 0:
                    main_balle.dy = 5
                    main_balle.dx = 0

            elif event.key == K_ESCAPE:
                arret()

        if event.type == pygame.QUIT:
            arret()
            
    main_balle.avance()

    if len(balles) < 500:
        for i in range(500-len(balles)):
            balles.append(Balle())

    time.sleep(0.02)
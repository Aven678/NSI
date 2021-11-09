#V4 Boules noires qui bougent, changement dans la règle du jeu : 
# si on touche un boule noire plus grosse, on meurt et le jeu se termine.
# Le but est de manger toutes les boules noires pour gagner

import pygame, sys
import time
from pygame.locals import *

from random import randint
import numpy as np

longueur,largeur = 1040,980

taille = 10

print("\nBonjour et bienvenue dans ce petit agar.io.")
print("Le principe est simple: mangez un maximum de balles pour grossir et manger les boules noires.")
print("Si vous êtes touché par une boule noire plus grosse que votre boule, le jeu s'arrête et vous avez perdu. \n")

class Balle:
    def __init__(self, taille = None, couleur = None, dx = None, dy = None, x=None, y = None):
        self.taille = 10 if taille == None else taille
        self.x = randint(5, longueur-(10 if taille == None else taille)) if x == None else x
        self.y = randint(5, longueur-(10 if taille == None else taille)) if y == None else y
        self.dx = dx if dx == None else dx
        self.dy = dy if dy == None else dy
        self.couleur = np.random.choice(range(230), size=3) if couleur == None else couleur
    
    def draw(self):
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.taille)
        
    def avance(self, player_ball):     #Uniquement utilisé par la balle contrôlée par l'utilisateur   
        self.draw()
        
        if self.x < self.taille/2 or self.x > longueur - self.taille/2 :
            self.dx = -self.dx
    
        if self.y < self.taille/2 or self.y > largeur - self.taille/2:
            self.dy = -self.dy
        
        self.x += self.dx
        self.y += self.dy
        
        self.collision(player_ball)
        
    def collision(self, player_ball): #Player_ball = False si il s'agit d'une boule noire
        if player_ball == False:
            if self.distanceAB(balle_joueur.x, balle_joueur.y) < self.taille:
                if self.taille > balle_joueur.taille:
                    print("Vous avez été éliminé par une boule noire!")
                    arret()

                else:
                    boules_noires.remove(self)
                    balle_joueur.taille += 0.2

                    if len(boules_noires) == 0:
                        print("Vous avez mangé toutes les boules noires ! \nVous avez gagné!")
                        arret()

            for boule in boules_noires: #Collision entre boules noires
                if self.distanceAB(boule.x,boule.y) < 2*self.taille:
                    self.dx,boule.dx = boule.dx,self.dx
                    self.dy,boule.dy = boule.dy,self.dy

        for balle in balles:
            if balle == self:
                continue
            
            if self.distanceAB(balle.x,balle.y) < self.taille:
                self.taille += 0.2
                balles.remove(balle)
        
    
    def distanceAB(self, xB, yB):
        return ((xB-self.x)**2+(yB-self.y)**2)**0.5


balles = [Balle() for x in range(500)]
boules_noires = [Balle(randint(5, 30), (0,0,0), randint(-2,2), randint(-2,2)) for x in range(10)]

balle_joueur = Balle(15,(255,0,0), 0, 0, longueur/2, largeur/2)

print("Il y a",len(balles)," balles dans la partie. ALLEZ ZÉ PARTI !")
print("Attention aux", len(boules_noires),"boules noires!")

pygame.display.init()
fenetre = pygame.display.set_mode((longueur, largeur))
fenetre.fill([0,0,0])


def arret():
    print("Fin du jeu, merci d'avoir joué.")
    pygame.display.quit()
    sys.exit()

while True:
    fenetre.fill([255,255,255])

    if balle_joueur.taille >= longueur:
        arret()

    for balle in balles:
        balle.draw()

    for boule in boules_noires:
        boule.avance(False)


    balle_joueur.draw()
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                pygame.key.set_repeat(40)
                if balle_joueur.x < longueur - balle_joueur.taille:
                    balle_joueur.x += 5

            if event.key == K_UP or event.key == K_z:
                pygame.key.set_repeat(40)
                if balle_joueur.y > 0 + balle_joueur.taille:
                    balle_joueur.y += -5

            if event.key == K_LEFT or event.key == K_q:
                pygame.key.set_repeat(40)
                if balle_joueur.x > 0 + balle_joueur.taille:
                    balle_joueur.x += -5

            if event.key == K_DOWN or event.key == K_s:
                pygame.key.set_repeat(40)
                if balle_joueur.y < largeur - balle_joueur.taille:
                    balle_joueur.y += 5

            if event.key == K_ESCAPE:
                arret()

        if event.type == pygame.QUIT:
            arret()
            
    balle_joueur.avance(True)

    if len(balles) < 500:
        for i in range(500-len(balles)):
            balles.append(Balle())

    time.sleep(0.02)
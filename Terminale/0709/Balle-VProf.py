import pygame, sys
import time
from pygame.locals import *

largeur = 320
hauteur = 480
taille = 20
dxA = 7
dyA = 4
dxB = -5
dyB = 3

pygame.display.init()
fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill([0,0,0])

xA = largeur // 2
yA = hauteur // 2
xB = largeur // 2
yB = hauteur // 2

couleur = (45,170,250)
couleurB = (155,17,250)

def distanceAB(xA, yA, xB, yB):
    return ((xA-xB)**2 + (yA-yB)**2)**0.5

while True :
    fenetre.fill([0,0,0])
    pygame.draw.circle(fenetre,couleurA,(xA,yA),taille)
    pygame.draw.circle(fenetre,couleurB,(xB,yB),taille)

    xA += dxA
    yA += dyA

    xB += dxB
    yB += dyB


    # rebond en haut ou en bas
    if yA < taille // 2 or yA > hauteur - taille // 2:
        dyA = -dyA

    # rebond à gauche ou à droite
    if xA < taille // 2 or xA > largeur - taille // 2:
        dxA = -dxA

    # rebond en haut ou en bas
    if yB < taille // 2 or yB > hauteur - taille // 2:
        dyB = -dyB

    # rebond à gauche ou à droite
    if xB < taille // 2 or xB > largeur - taille // 2:
        dxB = -dxB

    if distanceAB(xA, yA, xB, yB) < taille:
        print("collision")
        

    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


    time.sleep(0.03)

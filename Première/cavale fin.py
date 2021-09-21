import pygame
import random
import numpy as np

echiquier = np.zeros((8,8))

blanc = (255, 255, 255)
noir = (0, 0, 0)

cases = 80
pygame.init()
screen = pygame.display.set_mode((8 * cases, 8 * cases), cases)
pos = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1],[-1,-2],[1,-2],[2,-1]]
font = pygame.font.Font(None, 48)
nb_coups = 1


def damier():
    for i in range(8):
        for j in range(8):
            if (i+j)%2==1:
                pygame.draw.rect(screen, blanc, (cases * i, cases * j, cases, cases))

                if echiquier[i][j] != 0:
                    label = font.render(str(int(echiquier[i][j])), 1, (100,255,255))
                    screen.blit(label, (cases*(i+0.5), cases*(j+0.5)))
            else:
                pygame.draw.rect(screen, noir, (cases * i, cases * j, cases, cases))
                if echiquier[i][j] != 0:
                    label = font.render(str(int(echiquier[i][j])), 1, (100,255,255))
                    screen.blit(label, (cases*(i+0.5), cases*(j+0.5)))


def possible_ou_pas(Xi, Yi, X, Y):
    resultat = 0

    if 8 > X >= 0 == echiquier[X][Y] and 0 <= Y < 8:
        for j in range(8):
            if X == (Xi + pos[j][0]) and Y == (Yi + pos[j][1]):
                resultat = resultat + 1

    if resultat > 0:
        return True
    else:
        return False

image = pygame.image.load("Première/caval.gif")
image1 = pygame.transform.scale(image, (cases, cases))
damier()

Xt = random.randint(0, 7)
Yt = random.randint(0, 7)
echiquier[Xt][Yt] = 1
label = font.render(str(int(echiquier[Xt][Yt])), 1, (100,255,255))
screen.blit(label, (cases*(Xt+0.5), cases*(Yt+0.5)))

screen.blit(image1, (cases * Xt, cases * Yt))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user pressed the close button in the top corner of the window.
            print("A bientôt !")
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos_1 = pygame.mouse.get_pos()

            choiceX = int(float(pos_1[0] // 80))
            choiceY = int(float(pos_1[1] // 80))

            if possible_ou_pas(Xt, Yt, choiceX, choiceY) == 1:
                damier()
                screen.blit(image1, (cases * choiceX, cases * choiceY))
                nb_coups = nb_coups + 1
                echiquier[choiceX][choiceY] = nb_coups
                Xt = choiceX
                Yt = choiceY
            else:
                print("NON NON NON")

    pygame.display.flip()

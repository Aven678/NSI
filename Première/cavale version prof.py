import pygame
import random

n, p = 8, 8
coup = 0
blanc = (255, 255, 255)
noir = (0, 0, 0)
cases = 80
echiquier = [[0] * n for i in range(p)]
X1 = random.randint(0, n - 1)
Y1 = random.randint(0, p - 1)
pos = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]


########################################################################
def damier():
    i = 0
    j = 0
    for i in range(8):
        for j in range(8):
            labelx = int(cases * (i + 0.5))
            labely = int(cases * (j + 0.5))
            if (i + j) % 2 == 1:
                pygame.draw.rect(ecran, blanc, (cases * i, cases * j, cases, cases))
                if echiquier[i][j] != 0:
                    label = font.render(str(echiquier[i][j]), 1, (100, 255, 255))
                    ecran.blit(label, (labelx, labely))
            else:
                pygame.draw.rect(ecran, noir, (cases * i, cases * j, cases, cases))
                if echiquier[i][j] != 0:
                    label = font.render(str(echiquier[i][j]), 1, (100, 255, 255))
                    ecran.blit(label, (labelx, labely))


#######################################################################
def possible(X, Y):
    j = 0
    if ((X >= 0) and (X < 8) and (Y >= 0) and (Y < 8) and (echiquier[X][Y] == 0)):
        for k in range(8):
            if (X == X1 + pos[k][0] and Y == Y1 + pos[k][1]):
                j = j + 1

    if j != 0:
        return True, j
    else:
        return False, None


#########################################################################
def game_over(X, Y):
    fin = None
    for k in range(8):
        X = X1 + pos[k][0]
        Y = Y1 + pos[k][1]
        if possible(X, Y)[0] == True:
            fin = False
    return fin


#########################################################################


pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 48)
ecran = pygame.display.set_mode((640, 640))
image = pygame.image.load("Première/caval.gif")
image1 = pygame.transform.scale(image, (cases, cases))
damier()
ecran.blit(image1, (cases * X1, cases * Y1))
continuer = True
pos_mouse = []
##########################################################################
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user pressed the close button in the top corner of the window.
            print("A bientôt !")
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = event.pos

            X = pos_mouse[0] // 80
            Y = pos_mouse[1] // 80
            if possible(X, Y)[0] == True:
                coup = coup + 1
                print(coup)
                X1 = X
                Y1 = Y
                echiquier[X][Y] = coup
                damier()
                ecran.blit(image1, (cases * X1, cases * Y1))
                pygame.display.flip()
                if game_over(X, Y) != False:
                    print("game over")
                    ga = font.render("game over", 1, (255, 0, 0))
                    ecran.blit(ga, (320, 320))

    if event.type == pygame.KEYDOWN:
        continuer = False
    pygame.display.flip()

pygame.quit()
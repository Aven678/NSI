from turtle import *

def carre(cote):
    for k in range(4):
        forward(cote)
        right(90)


def motif(cote,n):
    if n == 0:
        return

    carre(cote)
    forward(cote/2)
    right(45)
    motif(cote/(2**0.5),n-1)

penup()        
goto(-80,-80)
pendown()
left(90)
speed(1)

motif(250,6)
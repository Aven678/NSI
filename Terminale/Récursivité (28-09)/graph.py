from turtle import *

def carre(cote):
    for k in range(4):
        forward(cote)
        right(90)

def losange(cote):
    forward(cote/2)
    right(45)

penup()        
goto(0,-80)
pendown()
left(90)
speed(0)

carre(250)
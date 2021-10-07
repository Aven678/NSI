from turtle import *

ang = 60

def floc(n,l):
    if n == 0:
        forward(l)
    else:
        floc(n-1,l/3)
        left(ang)
        floc(n-1,l/3)
        right(ang*2)
        floc(n-1,l/3)
        left(ang)
        floc(n-1,l/3)

def triangle(n,l):
    for i in range(6):
        left(ang)
        floc(2,l)
        right(ang*2)
        floc(2,l)

pendown()
triangle(3,100)

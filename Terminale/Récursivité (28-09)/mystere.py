import sys

sys.setrecursionlimit(1000000)

def mystere(n):
    if n == 0 :
        return 0
    else : 
        return n + mystere(n-1)

print(mystere(19384))
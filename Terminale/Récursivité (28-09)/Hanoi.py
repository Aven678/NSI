def hanoi(n, depart, inter, arrivee):
    if n == 1:
        print(depart,"vers",arrivee)
    else:
        hanoi(n-1,depart,arrivee,inter)
        print(depart,"vers",arrivee)
        hanoi(n-1, inter, depart, arrivee)


hanoi(4,"A","B","C")
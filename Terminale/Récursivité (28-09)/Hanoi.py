def hanoi(n, depart, inter, arrivee):
    if n == 1:
        print(depart,"vers",arrivee)
    else:
        hanoi(n-1,depart,arrivee,inter)
        print(depart,"vers",inter)
        hanoi(n-1, depart=inter, inter=depart, arrivee=arrivee)


hanoi(10,"A","B","C")
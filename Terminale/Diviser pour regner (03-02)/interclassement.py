def interclassement(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    i1 = 0
    i2 = 0
    lst_totale = []

    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst_totale.append(lst1[i1])
            i1 += 1
        else:
            lst_totale.append(lst2[i2])
            i2 += 1

    return lst_totale + lst1[i1:] + lst2[i2:]
    
def tri_fusion(lst):
    if len(lst) <= 1:
        return lst

    n = len(lst)//2
    return interclassement(tri_fusion(lst[:n]), tri_fusion(lst[n:]))
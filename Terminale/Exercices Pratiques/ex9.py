#Exo 9.1
def moyenne(lst):
    somme_coeff = 0
    somme_notes = 0

    for couple in lst:
        somme_notes += (couple[0] * couple[1])
        somme_coeff += couple[1]

    return somme_notes / somme_coeff

#Exo 9.2
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
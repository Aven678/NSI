#Ex 1
def moyenne(notes):
    sum_coef = 0
    sum_notes = 0

    for eval in notes:
        note = eval[0]
        coef = eval[1]

        sum_notes += (note*coef)
        sum_coef += coef

    return sum_notes/sum_coef

#Ex 2
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
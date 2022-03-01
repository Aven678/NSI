#Ex 1.1
def recherche(caractere, mot):
    i = 0
    for k in mot:
        if k == caractere:
            i += 1
    return i

#Ex 1.2
pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre-p, solution, i)
    else:
        return rendu_glouton(arendre, solution, i+1)
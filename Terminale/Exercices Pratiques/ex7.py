#Exo 7.1

def fibonnaci(n):
    resultats = {1:1, 2:1}

    if n in resultats:
        return resultats[n]

    for i in range(3,n+1):
        resultats[i] = resultats[i-1] + resultats[i-2]
        
    return resultats[n]
#Exo 7.1

def fibonnaci(n):
    resultats = {1:1, 2:1}
    for i in range(3,n+1):
        resultats[i] = resultats[i-1] + resultats[i-2]
        
    print(resultats[n])
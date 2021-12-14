import time

def createLst(size):
    return [2021 for i in range(size)]
 
def createDict(size):
    return {key:0 for key in range(size)}

n = 10**8
lst = createLst(n)
dico = createDict(n)
startTime = time.time()

test = 2022 in lst
pepene = time.time() - startTime

print("liste", pepene)
startTime = time.time()
test = -5 in dico
unPepene = time.time() - startTime
print("dictionnaire", unPepene)
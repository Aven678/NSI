# A part
for domino in sac:
    domino.dessine()
    
def nb_faces_compatible(d1, d2):
    faces = []
    if d1.faceA == d2.faceA:
        if d1.faceA is not faces:
            faces.append(d1.faceA)
            
            
    if d1.faceA == d2.faceB:
        faces+=1
    if d1.faceB == d2.faceA:
        faces += 1
    if d1.faceB == d2.faceB:
        faces += 1
        
    return faces

def check(face, d1):
    if d1.faceA == face or d1.faceB == face:
        return True
        
    return False

def chaine_la_plus_longue():
    chaine = []
    
    for domino in sac:
        chaine_temp = [domino]
        last_domino = domino
        last_faces = 0
        
        for d2 in sac:
            if d2 == domino:
                continue
            
            if last_faces != 0 and check(last_faces, d2) == False:
                continue
            
            if sont_compatibles(last_domino, d2):
                    
                chaine_temp.append(d2)
                last_domino = d2
            
        if len(chaine) < len(chaine_temp):
            print(len(chaine), len(chaine_temp))
            chaine = chaine_temp
            
    for domino in chaine:
        domino.dessine()
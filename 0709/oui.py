#1ère balle
    pygame.draw.circle(fenetre,couleur,(xA,yA),taille)     
        
            
    if xA < taille//2 or xA > longueur - taille //2:
        dx = -dx
    
    if yA < taille //2 or yA > largeur - taille //2:
        dy = -dy
        
    xA += dx
    yA += dy
    
    
    #2e balle
    pygame.draw.circle(fenetre,couleur2,(xB,yB),taille)
    
        
    xB += dx2
    yB += dy2
    
    if xB < taille//2 or xB > longueur - taille //2:
        dx2 = -dx2
    
    if yB < taille //2 or yB > largeur - taille //2:
        dy2 = -dy2
    
    if distanceAB(xA,yA,xB,yB) < taille:
        print("collision")
        dx,dx2 = dx2,dx
        dy,dy2 = dy2,dy
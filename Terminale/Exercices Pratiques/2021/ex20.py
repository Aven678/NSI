#Ex 20.1
def mini(releve, date):
    t_mini = releve[0]
    d_mini = date[0]
    for i in range(1,len(releve)):
        if t_mini > releve[i]:
            t_mini = releve[i]
            d_mini = date[i]

    return t_mini, d_mini

#Ex 20.2
def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
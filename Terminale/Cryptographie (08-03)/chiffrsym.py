def chiffre(message, masque):
    result = ""
    for k in range(len(message)):
        result += chr(ord(message[k]) ^ ord(masque[k]))

    return result
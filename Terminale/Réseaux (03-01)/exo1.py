def convert_ip_to_list(ip):
    """
    entrée : ip (string) 
    sortie : liste d'entiers
    """
    return [int(k) for k in ip.split(".")]

def test_convert_ip_to_list():
    assert convert_ip_to_list('192.168.0.1') == [192, 168, 0, 1]


def nb_to_binary_word(masque):
    """
    entrée : masque (int)
    sortie : string
    """
    return masque*'1' + (32-masque)* '0'
    
    

def test_nb_convert_to_binary_word():
    assert nb_to_binary_word(24) == '11111111111111111111111100000000'


def binary_word_to_list(word):
    """
    entrée : word (string de 32 caractères)
    sortie : liste de 4 entiers
    """
    # à vous
    return [int(word[8*i:(i+1)*8],2) for i in range(4)]
    



def test_binary_word_to_list():
    assert binary_word_to_list('11111111111111111111111100000000') == [255, 255, 255, 0]



def meme_sous_reseau(ip_a, ip_b, masque):
    """
    ip_a:  string contenant une IP (ex "192.168.0.1")
    ip_b : string contenant une IP
    masque : entier du masque en notation CIDR (ex : 24)
    renvoie un booléen indiquant si ip_a et ip_b sont dans
    le même sous-réseau
    """
    lstA = convert_ip_to_list(ip_a)
    lstB = convert_ip_to_list(ip_b)
    mask = binary_word_to_list(nb_to_binary_word(masque))

    resA = [lstA[i] & mask[i] for i in range(4)]
    resB = [lstB[i] & mask[i] for i in range(4)]

    return resA == resB


def test_meme_sous_reseau():
    assert meme_sous_reseau("192.168.0.1", "192.168.1.3", 24) == False
    assert meme_sous_reseau("192.168.0.1", "192.168.1.3", 20) == True
    assert meme_sous_reseau("192.168.0.1", "192.168.0.3", 30) == True

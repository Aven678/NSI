import hashlib

lst = open("extraitrockyou.txt").read().splitlines()
dico = {}

def inverse_md5(req):
    if req in dico:
        return dico[req]
    
    return "Not found"

for item in lst:
    dico[hashlib.md5(item.encode()).hexdigest()] = item

































    
    
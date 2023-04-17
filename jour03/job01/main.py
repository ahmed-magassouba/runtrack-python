import re
# config: utf-8
# file= open("output.txt", "r")
# print(file.read()) 
# file.close()

with open("domains.xml", "r",encoding='utf8') as file:
    count = 0
    for line in file:
        if "domain" in line:
            count += 1
            # print(line)
    print("le nombre de nom de dommaine est :",count)

    
# fonction de comparaison des mots avec le regex
def compare(mot):
    regex = re.compile(r"\b(\w+)\b")
    if re.findall(regex,mot):
        return True
    else:
        return False
    

with open("data.txt", "r") as file:
    count = 0
    regex = r"\b(\w+)\b" 
    # ligne = file.readlines() 
    # nbreLigne = len(ligne)
  
    # ligne2 = file.read().splitlines()
    # nbreLigne2 = len(ligne2)
    mots = file.read().strip().split()
    # nbreMots = len(mots)
    # print("le nombre de ligne est :",nbreLigne)
    # print("le nombre de mots est :",nbreMots)
    for mot in mots:
        if re.findall(regex,mot):
            count += 1
            # print(mot)
    print("le nombre de mots avec le regex est :",count)
   
    
import re

saisie = input("Veillez saisir un nombre entier : ")
saisie = int(saisie)


    

with open("data.txt", "r") as file:
    count = 0
    regex = r"^[a-zA-Z]{"+str(saisie)+"}$"
    mots = file.read().split()
    for mot in mots:
        if  re.match(regex,mot):
            count += 1
            # print(mot)
    print("le nombre de mots avec " + str(saisie) + "carractères est : ",count)
   
    
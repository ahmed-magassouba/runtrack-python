while True:
    saisie1= input("Veillez saisir votre premier chaine de carractère : ")
    if saisie1.isalpha():
        break
    else:
        print("La chaine de carractère doit être alphabétique.")
while True:
    saisie2= input("Veillez saisir votre deuxième chaine de carractère : ")
    if saisie2.isalpha():
        break
    else:
        print("La chaine de carractère doit être alphabétique.")

saisie1 = saisie1.lower()
saisie2 = saisie2.lower()

for i in saisie1:
    if i in saisie2:
        saisie2 = saisie2.replace(i,"",1)
    else:
        print(0)
        break


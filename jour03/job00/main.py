saisie=input("Entrer une chaine de carractère : ")
file = open("output.txt", "w") 
file.write(saisie) 
file.close()

# with open("output.txt", "w") as file:
#     file.write(saisie)
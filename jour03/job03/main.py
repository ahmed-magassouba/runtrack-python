import re
import matplotlib.pyplot as plt

plt.xlabel("Lettres")
plt.ylabel("Pourcentage (%)")
plt.title("Pourcentage d'apparition de chaque mot")




lettres=[]

with open("data.txt", "r") as file:
    # count = 0
    # regex = r"^[a-zA-Z]{"+str(saisie)+"}$"
    mots = file.read().split()
    
    witness = []
    count= []
    for mot in mots:
        for lettre in mot:
            lettre = lettre.lower()
            lettres.append(lettre)
                        # print(lettre)
    for i in lettres:
        if i not in witness:
            witness.append(i)
            count.append(lettres.count(i))
    print(witness , len(witness))
    print(count, len(count))

  
      
           
       
# creating the bar plot
plt.bar(witness, count, color ='blue',
        width = 1)    
plt.show()   
    
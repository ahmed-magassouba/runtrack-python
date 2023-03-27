tab=[]
for i in range(5):
   nombre = input("Entrez un nombre : ")
   nombre = int(nombre)
   tab.append(nombre)

tab.sort()
print(tab)
# config: utf-8
# file= open("output.txt", "r")
# print(file.read()) 
# file.close()

with open("output.txt", "r") as file:
    print(file.read())
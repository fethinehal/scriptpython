#Ecrire un programme qui choisi le plus grand nombre parmi deux nombres saisie
a = int(input("veuillez saisir le premier nombre: "),)
b = int(input("veuillez saisir le deuxième nombre: "))
if a>b:
    print("le plus grand nombre est: " + str(a))
elif (a==b):
    print("les nombres sont égaux")
else:
    print("le plus grand nombre est: " + str(b))
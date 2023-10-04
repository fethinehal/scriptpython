#trouver les plus grand nombre de trois nombre saisie
a = int(input("veuillez saisir le premier nombre: "),)
b = int(input("veuillez saisir le deuxième nombre: "))
c = int(input("veuillez saisir le troisième nombre: "))
if a>b & b>c:
    print("le plus grand nombre est: " + str(a))
elif b>c:
    print("le plus grand nombre est: " + str(b))
else:
    print("le plus grand nombre est: " + str(c))

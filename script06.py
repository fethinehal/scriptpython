#Décrire un programme qui va lire les données d'un employé a partir du clavier
#identifiant, nom, salaire, adresse, marié
status = bool(input("est ce que vous êtes marie?"))
o = input("true")
n = input("false")
a = int(input("veuillez saisire l'identifiant: "))
b = input("veuillez saisire le nom: ")
c = float(input("veuillez saisire le salaire: "))
d = input("veuillez saisire l'adresse: ")
e = input("veuillez saisire l'état civile: ")


print("l'identifiant: " + str(a) +"\nle nom: "+ str(b )+ "\nle salaire: " + str(c) + "\nl'adresse: " + str(d) + "\nl'état: " + str(e))
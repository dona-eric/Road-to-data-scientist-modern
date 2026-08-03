### pour aficher un message de bienvnu en python 

from collections import Counter
print("Welcome on MLAcademy")

### autres facons

print(f"Welcome to episode on python programming")



####### commennt declarer une varibales en python #################

# nom_eleve = str(input("VeuilleZr entrer votre nom: "))
# prenom_eleve = str(input("VeuilleZr entrer votre prenom: "))
# age_eleve = int(input("VeuilleZr entrer votre age: "))

# print(f"Bonjour {prenom_eleve} {nom_eleve}, vous avez {age_eleve} ans")


# ##### types de variables 

# """
# str : string(chaine de caracteres)
# float: nombre a virgule, des nombres flottants
# int: nombre entier
# bool
# """

# print(type(nom_eleve))
# print(type(prenom_eleve))
# print(type(age_eleve))


#####  exercices #####

# "nom, marche, prix d'un produit"
# nom_produit = str(input(f"Entrer le nom du produit:"))
# marche_produit = str(input(f"Entrer le marche du produit:"))
# prix_produit = float(input(f"Entrer le prix du produit:"))
# quantite_produit = int(input(f"Entrer la quantite du produit:"))

# print(f"Le produit {nom_produit} de marque {marche_produit} coute {prix_produit} FCFA")



#### arithmetique(operations)#####

# a = 0
# b = 5
# c = 10
# d = 3

# # adddition
# print(a+b)

# # soustraction
# print(b-a)

# # division
# print(c/b)
# print(a/d)

# # multiplication
# print(a*b)



# ##### exercices #######

# #calculer la superficie, le perimetre d'un rectangle

# longueur = float(input("Donner la longueur du rectangle: "))
# largeur = float(input("Donner la largeur du rectangle: "))

# # calcul
# superficie = longueur*largeur
# perimetre = (longueur+largeur)*2

# # affichage
# print(f"La superficie du rectangle est: {superficie} metres carres")
# print(f"Le perimetre du rectangle est: {perimetre} mètres")

#### fin des operations 


##### Les listes en python
##### les diffrentes matieres dun eleve de la classe de terminale


matieres = ["PCT", "maths", "svt", "geographie", "philosophie", 2]

print(matieres)

print(type(matieres))

## append 

matieres.append("anglais")
matieres.append("histoire")

print(matieres)
### premier element dune liste
print(matieres[0])

# 2 element
print(matieres[1])
## 03 elemeents ou indices d'une liste
print(matieres[2])

#### toois premier element de la liste 

print(matieres[::1])

### decroissannt 
decroissant = matieres.reverse()
print(decroissant)

# supprimer
matieres.remove(2)
print(matieres)

# supprimer pct
matieres.remove("PCT")
print(matieres)

### pop
matieres.pop(3)
print(matieres)

matieres.sort()
print(matieres)

### insert
matieres.insert(3, "pct")
print(matieres)

matieres.insert(1, "géographie")
print(matieres)



#### compter
# matieres.count()
print(len(matieres))

## clear
copie = matieres.copy()

copie.append("analyse")
copie.insert(3, "python")
print(copie)

copie.extend("jean")
print(copie)

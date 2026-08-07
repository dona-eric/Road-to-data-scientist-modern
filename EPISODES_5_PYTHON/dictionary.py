#### declarer un dictionnaire ,

#### notes d'un eleve de la classe de terminale

notes_eleve = {
    "Anglais":15,
    "Maths":8,
    "Svt":12,
    "PCT":18,
    "Histoire":10,
    "Geographie":15,
    "Philosophie":12
}

# types de données utilisés
print(type(notes_eleve))

# print le dictionnaire
print(notes_eleve)

# acceder un element du dictionnaire 
print(notes_eleve["Histoire"])

# ajouter un elelmet au docitionnaire
notes_eleve['EPS']=17
# modiffierla valeur d'un element dasn un dictionnaire
notes_eleve["Maths"]=14

notes_eleve["maths"]=19

# supprimler un element dans unn dictionnaire
notes_eleve.pop("PCT")
print((notes_eleve))

# les differentes methodes d'un dictionnaire
print(notes_eleve.keys())
# les valeurs de dictionnaire uniqquement
print(notes_eleve.values())

# les valeurs de dictionnaire uniqquement et les cles
print(notes_eleve.items())

print(notes_eleve.get("Anglais"))
print(notes_eleve.get("EPS"))

copie = notes_eleve.copy()
print(copie)

# supprimer tous les elements du dictionnaire
notes_eleve.clear()
print(notes_eleve)












"""     EXERCICEIIECIEIEIEIEIECIE         """

"""
📚 Exercice 10 — Projet Final (Niveau Avancé) ⭐⭐⭐⭐⭐

Créer une application de gestion d'une bibliothèque numérique utilisant les dictionnaires.

Chaque livre possède :

ISBN
titre
auteur
année
catégorie
nombre d'exemplaires

L'application doit proposer un menu :

1. Ajouter un livre

2. Rechercher un livre

3. Modifier un livre

4. Supprimer un livre

5. Emprunter un livre

6. Retourner un livre

7. Afficher tous les livres

8. Sauvegarder les données (JSON)

9. Charger les données
"""

























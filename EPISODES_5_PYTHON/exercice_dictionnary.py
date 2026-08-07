"""
 Créer un dictionnaire représentant un étudiant avec les informations suivantes :

Nom : Eric
Âge : 25
Pays : Bénin
Filière : Data Science
Questions
Afficher le dictionnaire.
Afficher uniquement le nom.
Afficher uniquement le pays.
Modifier l'âge en 26.
Ajouter la clé ville avec la valeur Cotonou.
Supprimer la clé filière.
Afficher toutes les clés.
Afficher toutes les valeurs.

"""


data = {}


# ajuter les element cle-valeurs aux dictionnaire
data.update(
    {
        'Nom': "Eric",
        "age":25,
        "country": "Benin",
        "filiere": "Data science"
    }
)


# afficher uniqueentle nom
print(data.get("Nom"))
""" ou"""
print(data["country"])

"=## modifier l'age"
data['age']=26
print(data)

data.update(
    {"age":27}
)
print(data)

# ajouter la clé ville = cotonou
data['ville']="cotonou"

print(data)

data.update({"ville":"cotonou"})
print(data)

#supprimet la clé filiere
data.pop("filiere")
print(data)

# afficher toutes les clés 
print(data.keys(),data.values())


""" autres exercices :


📚 Exercice 8 — Dictionnaires imbriqués ⭐⭐⭐⭐

Créer

entreprise = {}

Chaque employé possède
*âge
*poste
*salaire

"""

entreprise = {}

entreprise.update(
    {
        "Jean":{
            "Age":25,
            "Poste":"AI engineer",
            "Salaire":250000
        },

        "Peace":{
            "Age":23,
            "Poste":"Data analyst",
            "Salaire":150000
        },

        "Inès":{
            "Age":35,
            "Poste":"Comptable Financier",
            "Salaire":120000
        }
    }
)
print(type(entreprise))

### ajouter un employé 

entreprise.update({
    "Dupont":{
        "Age":22,
        "Poste": "Developpeur",
        "Salaire":200000
    }
})
print(entreprise)

### modifier le salaire de jean à 700k

entreprise['Jean']["Salaire"]=700000
print(entreprise)

### mettre l'age , le poste et le salaire de dupont

entreprise["Dupont"].update({
    "Age": 24,
    "Poste": "Lead Developer",
    "Salaire": 500000
})

print(entreprise)

#### supprimer jean de la base d eonnées

entreprise.pop('Jean')
print(entreprise)

# afficher la liste des employés

print(entreprise.keys())


# afficher le salaire moyen

salaire = [s["Salaire"] for s in entreprise.values()]
print(salaire)
moyenne = sum(salaire)/len(salaire)
print(moyenne)



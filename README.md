
# ✅*Machine Learning Engineer Roadmap*


## 🚀 Machine Learning Engineer Roadmap (Débutant → Avancé)

Bienvenue dans ce dépôt de référence destiné à toute personne souhaitant devenir **Machine Learning Engineer**, en partant **de zéro** jusqu’à un **niveau avancé**.

🎯 Ce dépot est pensé comme une **feuille de route pratique**, enrichie **cours après cours**, avec des **exemples de code, ressources, exercices, notebooks, projets**, et plus encore instructif pour permettre
aux désirés embrasser une carrière d'Ingénieur en Machine Learning.

---

## 🧠 Objectifs du dépôt

- Offrir une **structure claire et progressive** d'apprentissage
- Documenter chaque concept appris (avec explication + code)
- Guider toute personne motivée à devenir **ML Engineer**
- Fournir des **ressources complémentaires** (articles, vidéos, PDF)

---

## 📚 Organisation du contenu

Le dépôt est divisé en **niveaux de difficulté**, chacun structuré en modules :
```
📂 niveau_debutant/
   ├── 01_structures_donnees/
   ├── 02_Base_Programmation_Python/
   ├── 03_Python_fondamentaux/
   ├── 04_Principes_fondamentaux_SQL/
   ├── 05_Introduction_Scripts_Bash/
   ├── 06_Introduction_Docker/
   ├── 07_Introduction_base_de_données/
   ├── 08_Docker_Intermédiaire/
   ├── 09_Architecture_moderne_des_données/
   ├── 10_Concepts_Conteneurisation_and_Virtualisation/
   ├── 11_Concepts_NoSQL/
   ├── 12_Building_API_Python_FastAPI/
   ├── 13_Big_Data_with_PySpark/
   └── README.md

📂 niveau_intermediaire/
   ├── 01_regression_logistique/
   ├── 02_arbre_decision/
   ├── 03_pipeline_sklearn/
   └── README.md

📂 niveau_avance/
   ├── 01_deploiement_model_fastapi/
   ├── 02_mle_avec_mlflow/
   ├── 03_distribue_pyspark/
   └── README.md

📂 projets_end_to_end/
   ├── projet_fraude_credit_card/
   ├── chatbot_educatif/
   └── dashboard_dash_streamlit/

📂 ressources/
   ├── articles/
   ├── cours/
   └── liens_utiles.md
```
---

## 🛠 Technologies abordées

* Python 🐍
* NumPy / Pandas
* Matplotlib / Seaborn / Plotly
* Scikit-learn
* FastAPI / Flask
* Streamlit / Dash / Gradio
* Spark (PySpark)
* MLflow / Weights & Biases
* Docker / Git / CI-CD
* Cloud (GCP / AWS / DigitalOcean)

---

## 🔗 Ressources recommandées

| Thème                           | Lien                                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| Python pour débutants           | [OpenClassrooms](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python) |
| Machine Learning                | [Cours Andrew Ng (Coursera)](https://www.coursera.org/learn/machine-learning)                  |
| MLOps                           | [MadeWithML](https://madewithml.com/)                                                          |
| Structures de données en Python | [RealPython](https://realpython.com/python-data-structures/)                                   |

Tu peux aussi consulter mes **[articles Medium](#)** ou mon [portfolio](https://dona-eric.github.io) pour plus d’infos.

---

## 🧩 Projets en vedette

* 🧠 [Chatbot éducatif IA sur WhatsApp](projets_end_to_end/chatbot_educatif/)
* 💳 [Détection de fraude sur cartes bancaires](projets_end_to_end/projet_fraude_credit_card/)
* 📈 [Dashboard interactif COVID-19 avec Dash](projets_end_to_end/dashboard_dash_streamlit/)

---

## 📌 Contribuer

Ce projet est aussi un **document vivant**. Si tu veux :

* Proposer une correction ou amélioration
* Ajouter un exemple ou ressource
* Contribuer à un module

... crée une *pull request* ou ouvre une *issue* 🙌

---

## 📫 Me contacter

* 💼 [LinkedIn](https://linkedin.com/in/dona-erick)
* 📧 [donaerickoulodji@gmail.com](mailto:donaerickoulodji@gmail.com)
* 🐙 [GitHub](https://github.com/dona-eric)
* 📝 [Medium](https://medium.com/@koulodjiric)
* 🌐 [Portfolio](https://dona-eric.github.io)


---

## 🔖 Licence

Ce projet est sous Apache LICENSE Version 2.0.
Tu es libre de l'utiliser, le modifier et le partager.

---

## ⭐ Donne une étoile !

Si ce repo t’aide, pense à laisser une ⭐ pour soutenir ce travail et le rendre plus visible à d’autres !


---
## 📝 Notes

Ce dépôt est en constante évolution. N'hésite pas à revenir régulièrement pour découvrir de nouveaux modules, ressources et projets.



Comment fonctionnent les Transformers ?
Poser une question
Dans cette section, nous examinerons l'architecture des modèles Transformer et approfondirons les concepts d'attention, d'architecture encodeur-décodeur, et plus encore.

🚀 On passe à la vitesse supérieure ! Cette section est détaillée et technique, alors ne vous inquiétez pas si vous ne comprenez pas tout du premier coup. Nous reviendrons sur ces concepts plus tard dans le cours.

Un peu d'histoire des Transformers
Voici quelques points de repère dans la (courte) histoire des modèles Transformers :

Brève chronologie des modèles Transformers.
L' architecture Transformer a été introduite en juin 2017. Les recherches initiales portaient sur les tâches de traduction. Ont suivi l'introduction de plusieurs modèles influents, notamment :

Juin 2018 : GPT , le premier modèle Transformer pré-entraîné, a été utilisé pour l’ajustement fin sur diverses tâches de traitement automatique du langage naturel et a obtenu des résultats de pointe.

Octobre 2018 : BERT , un autre grand modèle pré-entraîné, celui-ci conçu pour produire de meilleurs résumés de phrases (plus de détails à ce sujet dans le chapitre suivant !)

Février 2019 : GPT-2 , une version améliorée (et plus importante) de GPT, n’a pas été immédiatement publiée en raison de préoccupations éthiques.

Octobre 2019 : T5 , une implémentation multitâche de l'architecture Transformer séquence-à-séquence.

Mai 2020 , GPT-3 , une version encore plus grande de GPT-2 capable de réaliser de bonnes performances sur une variété de tâches sans avoir besoin d'un réglage fin (appelé apprentissage zéro-shot ).

Janvier 2022 : InstructGPT , une version de GPT-3 entraînée à mieux suivre les instructions.

Janvier 2023 : Llama , un modèle de langage de grande envergure capable de générer du texte dans diverses langues.

Mars 2023 : Mistral , un modèle de langage de 7 milliards de paramètres qui surpasse Llama 2 13B sur tous les benchmarks évalués, tirant parti de l'attention de requête groupée pour une inférence plus rapide et de l'attention de fenêtre glissante pour gérer des séquences de longueur arbitraire.

Mai 2024 : Gemma 2 , une famille de modèles ouverts légers et de pointe allant de 2B à 27B paramètres qui intègrent des attentions locales-globales entrelacées et une attention de requête de groupe, avec des modèles plus petits entraînés à l'aide de la distillation des connaissances pour offrir des performances compétitives avec des modèles 2 à 3 fois plus grands.

Novembre 2024 : SmolLM2 , un modèle de langage compact de pointe (de 135 millions à 1,7 milliard de paramètres) qui atteint des performances impressionnantes malgré sa taille compacte et ouvre de nouvelles possibilités pour les appareils mobiles et périphériques.

Cette liste est loin d'être exhaustive et vise simplement à mettre en lumière quelques-uns des différents modèles de Transformers. De manière générale, on peut les regrouper en trois catégories :

Modèles de type GPT (également appelés modèles Transformer autorégressifs )
Modèles de type BERT (également appelés modèles Transformer à auto-encodage )
Modèles de type T5 (également appelés modèles Transformer séquence-à-séquence )
Nous étudierons ces familles plus en détail ultérieurement.

Les transformateurs sont des modèles de langage
Tous les modèles Transformer mentionnés ci-dessus (GPT, BERT, T5, etc.) ont été entraînés en tant que modèles de langage . Cela signifie qu'ils ont été entraînés sur de grandes quantités de texte brut de manière auto-supervisée.

L'apprentissage auto-supervisé est un type d'entraînement où l'objectif est calculé automatiquement à partir des entrées du modèle. Autrement dit, l'intervention humaine pour étiqueter les données est superflue !

Ce type de modèle développe une compréhension statistique du langage sur lequel il a été entraîné, mais il est moins utile pour des tâches pratiques spécifiques. C'est pourquoi le modèle pré-entraîné général subit ensuite un processus appelé apprentissage par transfert ou ajustement fin . Au cours de ce processus, le modèle est ajusté de manière supervisée — c'est-à-dire à l'aide d'annotations humaines — sur une tâche donnée.

Un exemple de tâche consiste à prédire le mot suivant dans une phrase après avoir lu les n mots précédents. On parle alors de modélisation causale du langage, car la sortie dépend des entrées passées et présentes, mais pas des entrées futures.

Exemple de modélisation causale du langage dans lequel le mot suivant d'une phrase est prédit.
Un autre exemple est la modélisation du langage masqué , dans laquelle le modèle prédit un mot masqué dans la phrase.

Exemple de modélisation du langage masqué dans lequel un mot masqué d'une phrase est prédit.
Les Transformers sont de grands modèles
Hormis quelques exceptions (comme DistilBERT), la stratégie générale pour obtenir de meilleures performances consiste à augmenter la taille des modèles ainsi que la quantité de données sur lesquelles ils sont pré-entraînés.

Nombre de paramètres des modèles de transformateurs récents
Malheureusement, l'entraînement d'un modèle, surtout s'il est de grande taille, nécessite une quantité importante de données. Cela s'avère très coûteux en temps et en ressources de calcul. Cela a même un impact environnemental, comme le montre le graphique suivant.

L'empreinte carbone d'un modèle de langage de grande taille.

Il s'agit ici d'un projet portant sur un modèle (de très grande envergure) mené par une équipe qui s'efforce de réduire l'impact environnemental du pré-entraînement. L'empreinte écologique liée à l'exécution de nombreux essais pour obtenir les hyperparamètres optimaux serait encore plus importante.

Imaginez si, chaque fois qu'une équipe de recherche, une association étudiante ou une entreprise souhaitait entraîner un modèle, elle devait le faire de zéro. Cela engendrerait des coûts mondiaux énormes et inutiles !

C’est pourquoi le partage des modèles de langage est primordial : le partage des poids entraînés et la construction sur la base de poids déjà entraînés réduisent le coût global de calcul et l’empreinte carbone de la communauté.

D'ailleurs, vous pouvez évaluer l'empreinte carbone de l'entraînement de vos modèles grâce à plusieurs outils. Par exemple , ML CO2 Impact ou Code Carbon , intégré à 🤗 Transformers. Pour en savoir plus, consultez cet article de blog qui vous expliquera comment générer un emissions.csvfichier contenant une estimation de l'empreinte carbone de votre entraînement, ainsi que la documentation de 🤗 Transformers sur ce sujet.

Transfert d'apprentissage

Le préentraînement consiste à entraîner un modèle à partir de zéro : les poids sont initialisés aléatoirement et l’entraînement commence sans aucune connaissance préalable.

Le préentraînement d'un modèle de langage est coûteux en temps et en argent.
Ce pré-entraînement est généralement effectué sur de très grandes quantités de données. Par conséquent, il nécessite un corpus de données très important et l'entraînement peut prendre jusqu'à plusieurs semaines.

Le fine-tuning , en revanche, est l'entraînement effectué après le pré-entraînement d'un modèle. Pour réaliser un fine-tuning, on commence par acquérir un modèle de langage pré-entraîné, puis on effectue un entraînement supplémentaire avec un jeu de données spécifique à la tâche. Attendez… pourquoi ne pas simplement entraîner le modèle pour le cas d'utilisation final dès le départ (à partir de zéro ) ? Il y a plusieurs raisons :

Le modèle pré-entraîné a déjà été entraîné sur un ensemble de données présentant certaines similarités avec l'ensemble de données d'ajustement fin. Le processus d'ajustement fin peut ainsi tirer parti des connaissances acquises par le modèle initial lors du pré-entraînement (par exemple, pour les problèmes de traitement automatique du langage naturel, le modèle pré-entraîné aura une certaine compréhension statistique du langage utilisé pour la tâche).
Comme le modèle pré-entraîné a déjà été entraîné sur une grande quantité de données, le réglage fin nécessite beaucoup moins de données pour obtenir des résultats corrects.
Pour la même raison, le temps et les ressources nécessaires pour obtenir de bons résultats sont bien moindres.
Par exemple, on pourrait utiliser un modèle pré-entraîné sur la langue anglaise, puis l'affiner sur un corpus arXiv, obtenant ainsi un modèle destiné à la recherche scientifique. Cet affinement ne nécessitera qu'une quantité limitée de données : les connaissances acquises par le modèle pré-entraîné sont « transférées », d'où le terme d'apprentissage par transfert .

Le réglage fin d'un modèle de langage est moins coûteux que le préentraînement, tant en temps qu'en argent.
L'ajustement fin d'un modèle engendre donc des coûts moindres en temps, en données, en argent et en environnement. Il est également plus rapide et plus facile d'itérer sur différentes méthodes d'ajustement fin, car l'entraînement est moins contraignant qu'un pré-entraînement complet.

Ce processus permettra également d'obtenir de meilleurs résultats qu'un entraînement à partir de zéro (sauf si vous disposez de beaucoup de données), c'est pourquoi vous devriez toujours essayer d'utiliser un modèle pré-entraîné — aussi proche que possible de la tâche à accomplir — et de l'affiner.

Architecture générale des transformateurs
Dans cette section, nous aborderons l'architecture générale du modèle Transformer. Si certains concepts vous semblent obscurs, ne vous inquiétez pas : des sections détaillées, couvrant chaque composant, seront présentées ultérieurement.


Le modèle est principalement composé de deux blocs :

Encodeur (à gauche) : L’encodeur reçoit une entrée et en construit une représentation (ses caractéristiques). Cela signifie que le modèle est optimisé pour comprendre l’entrée.
Décodeur (à droite) : Le décodeur utilise la représentation (caractéristiques) de l’encodeur ainsi que d’autres entrées pour générer une séquence cible. Autrement dit, le modèle est optimisé pour la génération de sorties.
Architecture des modèles de Transformers
Chacune de ces pièces peut être utilisée indépendamment, selon la tâche :

Modèles d'encodeur uniquement : adaptés aux tâches nécessitant une compréhension de l'entrée, telles que la classification de phrases et la reconnaissance d'entités nommées.
Modèles de décodeur uniquement : adaptés aux tâches génératives telles que la génération de texte.
Modèles encodeur-décodeur ou modèles séquence-à-séquence : adaptés aux tâches génératives nécessitant une entrée, telles que la traduction ou le résumé.
Nous examinerons ces architectures plus en détail dans les sections suivantes.

Couches d'attention
Une caractéristique essentielle des modèles Transformer est leur construction à l'aide de couches spéciales appelées couches d'attention . D'ailleurs, le titre de l'article présentant l'architecture Transformer était « L'attention est tout ce dont vous avez besoin » ! Nous explorerons les détails des couches d'attention plus tard dans ce cours ; pour l'instant, il vous suffit de retenir que cette couche indique au modèle de porter une attention particulière à certains mots de la phrase qui lui est fournie (et d'ignorer plus ou moins les autres) lors du traitement de la représentation de chaque mot.

Pour mieux comprendre, prenons l'exemple de la traduction d'un texte de l'anglais vers le français. Face à la phrase « You like this course », un modèle de traduction devra également prendre en compte le pronom « You » pour traduire correctement « like », car en français, le verbe « like » se conjugue différemment selon le sujet. Le reste de la phrase, en revanche, n'est pas pertinent pour la traduction de ce mot. De même, pour traduire « this », le modèle devra aussi tenir compte du mot « course », car sa traduction diffère selon que le nom auquel il est associé est masculin ou féminin. Là encore, les autres mots de la phrase n'ont aucune incidence sur la traduction de « course ». Avec des phrases plus complexes (et des règles grammaticales plus complexes), le modèle devra accorder une attention particulière aux mots qui peuvent apparaître plus loin dans la phrase afin de traduire correctement chaque mot.

Le même concept s'applique à toute tâche liée au langage naturel : un mot a en lui-même une signification, mais cette signification est profondément influencée par le contexte, qui peut être n'importe quel autre mot (ou mots) avant ou après le mot étudié.

Maintenant que vous avez une idée de ce que sont les couches d'attention, examinons de plus près l'architecture Transformer.

L'architecture d'origine
L'architecture Transformer a été initialement conçue pour la traduction. Lors de l'entraînement, l'encodeur reçoit des entrées (phrases) dans une langue donnée, tandis que le décodeur reçoit les mêmes phrases dans la langue cible. Dans l'encodeur, les couches d'attention peuvent exploiter tous les mots d'une phrase (puisque, comme nous l'avons vu, la traduction d'un mot dépend aussi bien de ce qui le précède que de ce qui le suit dans la phrase). Le décodeur, quant à lui, fonctionne séquentiellement et ne peut s'intéresser qu'aux mots de la phrase qu'il a déjà traduits (donc uniquement aux mots précédant le mot en cours de génération). Par exemple, une fois les trois premiers mots de la langue cible prédits, on les transmet au décodeur qui utilise alors toutes les entrées de l'encodeur pour tenter de prédire le quatrième mot.

Pour accélérer l'entraînement (lorsque le modèle a accès aux phrases cibles), le décodeur reçoit l'intégralité de la phrase cible, mais sans pouvoir utiliser les mots suivants (s'il avait accès au mot en position 2 pour prédire ce mot, la tâche serait beaucoup plus simple !). Par exemple, pour prédire le quatrième mot, la couche d'attention n'aura accès qu'aux mots en positions 1 à 3.

L'architecture originale du Transformer ressemblait à ceci, avec l'encodeur à gauche et le décodeur à droite :

Architecture des modèles de Transformers
Notez que la première couche d'attention d'un bloc décodeur prend en compte toutes les entrées (passées) du décodeur, tandis que la seconde couche d'attention utilise la sortie de l'encodeur. Elle peut ainsi accéder à la phrase d'entrée complète pour prédire au mieux le mot courant. Ceci est très utile car différentes langues peuvent avoir des règles grammaticales qui placent les mots dans un ordre différent, ou un contexte fourni plus loin dans la phrase peut aider à déterminer la meilleure traduction d'un mot donné.

Le masque d'attention peut également être utilisé dans l'encodeur/décodeur pour empêcher le modèle de prêter attention à certains mots spéciaux — par exemple, le mot de remplissage spécial utilisé pour que toutes les entrées aient la même longueur lors du regroupement des phrases.

Architectures vs. points de contrôle
Dans ce cours, nous aborderons les modèles Transformer et vous rencontrerez les termes « architectures » , « points de contrôle » et « modèles » . Ces termes ont des significations légèrement différentes :

Architecture : Il s'agit du squelette du modèle — la définition de chaque couche et de chaque opération qui se déroule au sein du modèle.
Points de contrôle : Il s’agit des poids qui seront chargés dans une architecture donnée.
Modèle : Ce terme générique est moins précis que « architecture » ​​ou « point de contrôle » : il peut désigner les deux. Ce cours précisera « architecture » ​​ou « point de contrôle » lorsque cela sera pertinent afin d’éviter toute ambiguïté.
Par exemple, BERT est une architecture, tandis que ` bert-base-casedcheckpoint`, un ensemble de poids entraînés par l'équipe Google pour la première version de BERT, est un point de contrôle. On peut cependant dire indifféremment « le modèle BERT » ou « le bert-base-casedmodèle ».
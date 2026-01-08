# 📊 Projet Power BI – Analyse des demandes de crédit

Le Crédit Breton

## 🧠 Présentation du projet

Ce projet a été réalisé dans le cadre d’un cours Power BI suivi sur OpenClassrooms.
Il porte sur l’analyse des demandes de crédit d’un établissement bancaire fictif nommé Le Crédit Breton.

L’objectif principal est de transformer des données brutes en informations exploitables afin de mieux comprendre :

- le profil des clients,

- leurs situations professionnelle et familiale,

- les caractéristiques des demandes de prêt,

- les tendances temporelles et géographiques.

## 🔒 Confidentialité & anonymisation

Les données fournies dans le cadre du cours n’étaient pas anonymisées.

Avant toute analyse :

- suppression des noms et prénoms,

- conservation uniquement d’identifiants clients,

- standardisation des catégories sensibles,

- aucune donnée personnelle identifiable n’est utilisée dans le rapport final.

👉 Cette étape respecte les bonnes pratiques RGPD et la déontologie Data.

## 🛠️ Outils & technologies

- Power BI Desktop

- Power Query (langage M)

- Excel (source de données)

- Modélisation en étoile

- Git / GitHub (valorisation du projet)

## 📁 Source des données

Fichier Excel : Dataset_cours_Power_BI.xlsx

Tables disponibles :

- Demandes de prêt

- Situation professionnelle

- Situation familiale

- Apports

- Agences

- Dates (créée manuellement)

## 🔄 Démarche projet (A → Z) :

 - 1️⃣ Importation des données : 

- Import des différentes feuilles Excel dans Power BI

- Promotion des en-têtes

- Vérification de la cohérence des champs

- Détection des valeurs manquantes ou incohérentes

 - 2️⃣ Nettoyage & transformation des données (Power Query) :

Chaque table a été nettoyée et préparée individuellement.

Exemple : Table Situation professionnelle

Transformations réalisées :

- promotion des en-têtes,

- typage des colonnes,

- harmonisation des libellés du statut d’emploi,

- nettoyage des valeurs textuelles.

let 
    Source = Excel.Workbook(File.Contents("Dataset_cours_Power_BI.xlsx"), null, true),
    #"Situation pro_Sheet" = Source{[Item="Situation pro",Kind="Sheet"]}[Data],
    #"En-têtes promus" = Table.PromoteHeaders(#"Situation pro_Sheet", [PromoteAllScalars=true]),
    #"Type modifié" = Table.TransformColumnTypes(
        #"En-têtes promus",
        {
            {"Numéro client", Int64.Type},
            {"Catégorie socioprofessionnelle", type text},
            {"Statut d'emploi", type text},
            {"Régularité des revenus", type text},
            {"Revenu mensuel moyen", type number}
        }
    ),
    #"Valeur remplacée" = Table.ReplaceValue(
        #"Type modifié",
        "Salariés : contrat à durée indéterminée",
        "Salariés : CDI",
        Replacer.ReplaceText,
        {"Statut d'emploi"}
    ),
    #"Valeur remplacée1" = Table.ReplaceValue(
        #"Valeur remplacée",
        "Salariés : contrat à durée déterminée",
        "Salariés : CDD",
        Replacer.ReplaceText,
        {"Statut d'emploi"}
    )
in
    #"Valeur remplacée1"


## 👉 Objectif : obtenir des données propres, cohérentes et prêtes pour l’analyse.

 - 3️⃣ Création d’une table de dates

Une table de dates dédiée a été créée afin de permettre des analyses temporelles robustes.

Champs de la table Dates :

  - Date

- Année

- Mois

- NumMois

- Année-Mois

Objectifs :

- centraliser toutes les informations calendaires,

- faciliter les filtres et les analyses temporelles,

- respecter les bonnes pratiques BI.

 - 4️⃣ Modélisation des données

Le modèle suit une architecture en étoile.

#### ⭐ Table de faits

Demandes de prêt

#### 📐 Tables de dimensions

- Situation professionnelle

- Situation familiale

- Agences

- Apports

- Dates

#### Relations

1 client → plusieurs demandes

1 agence → plusieurs demandes

1 date → plusieurs demandes
Relations en 1 → * (un-à-plusieurs) avec filtrage à sens unique.

👉 Ce modèle garantit :

- de bonnes performances,

- une lecture métier claire,

- des mesures fiables.

## 📈 Analyses & visualisations
🔹 1. Répartition des demandes par statut professionnel

Constat :

La majorité des demandes provient de clients en CDI.

Les profils en CDD ou revenus irréguliers sont moins représentés.

Interprétation :

La stabilité professionnelle est un facteur clé dans l’accès au crédit.

🔹 2. Montant moyen des prêts par catégorie socioprofessionnelle

Constat :

Les cadres et professions intermédiaires demandent des montants plus élevés.

Les employés et ouvriers ont des montants plus modestes.

Interprétation :

Le niveau de revenu influence directement la capacité d’emprunt.

🔹 3. Impact de la situation familiale

Constat :

Les clients avec plusieurs enfants à charge sollicitent des montants plus importants.

Les célibataires ont des durées de prêt plus courtes.

Interprétation :

Les besoins financiers varient fortement selon la composition du foyer.

🔹 4. Analyse temporelle des demandes

Constat :

Certaines périodes de l’année concentrent plus de demandes.

Interprétation :

Ces variations peuvent être liées à des projets immobiliers ou à des effets saisonniers.

## ✅ Compétences démontrées

- Nettoyage et préparation des données

- Anonymisation de données sensibles

- Power Query (langage M)

- Modélisation de données (schéma en étoile)

- Création d’une table de dates

- Analyse métier

- Data visualisation avec Power BI

- Restitution claire et structurée

## 📌 Conclusion

Ce projet illustre un processus complet de Data Analysis, de la donnée brute jusqu’à l’analyse décisionnelle.
Il met en avant ma capacité à :

- structurer et fiabiliser des données,

- comprendre un besoin métier,

- produire des analyses claires et pertinentes à l’aide de Power BI.

## 💡 Axes d’amélioration possibles

- Ajout de mesures DAX avancées

- Analyse prédictive simple

- Comparaison inter-agences

- Optimisation du modèle pour un volume de données plus important

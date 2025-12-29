#!/usr/bin/env python
# coding: utf-8

# # Import de librairies

# In[3]:


import pandas as pd #manipulation et analyse de données
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


# # Import de données
# 

# In[38]:


# Chargé les données csv
df = pd.read_csv("OnlineRetail.csv", encoding="ISO-8859-1")


# # Analyse exploratoire

# aperçu des données

# In[24]:


df.head() # Aperçu des 5 premières lignes
df.info()          # Types de données et valeurs manquantes
df.describe()      # Statistiques descriptives (numériques)


# # Valeurs manquantes ?

# In[14]:


df.isnull().sum()


# # Interprétation

# Interprétation
# La plupart des colonnes n'ont pas de valeurs manquantes. 
# 
# Colonnes avec valeurs manquantes :
# 
# - Description a 1 454 valeurs manquantes : il manque des descriptions produits.
# 
# - CustomerID a 135 080 valeurs manquantes : donc une grande partie des transactions n’ont pas d’identifiant client associé. 
# C’est courant dans certains datasets e-commerce (par exemple pour les visiteurs anonymes).

# # Valeurs abérrantes 

# In[23]:


df[(df['Quantity'] <= 0)] # Vérifier s'il ya des valeurs négatives pour les quantités
df[df['UnitPrice'] <= 0]  # Vérifier s'il ya des valeurs négatives pour les prix


# NB : 
#     Notre base de données présentent deux spécificités :
#         Les données sdont les quantités et/ou les prix sont négatifs sont des données liées aux remboursements et aux avoirs.
#         Les données dont les quantités avosinent les 9999 sont probablement des Commande en gros ou des erreurs.
# 

# # Présence de doublons

# In[26]:


df.duplicated().sum() # il y'a 5 268 Doublons dans les données.


# # Suprimer les doublons 

# In[27]:


df_clean = df.drop_duplicates()


# # Distribution des données par pays 
# 

# In[29]:


import matplotlib.pyplot as plt

# Compter les transactions par pays
pays_counts = df_clean['Country'].value_counts()

# Affichage
plt.figure(figsize=(12,6))
pays_counts.plot(kind='bar')
plt.title("Nombre de transactions par pays")
plt.xlabel("Pays")
plt.ylabel("Nombre de transactions")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[31]:


df_clean['Country'].nunique() # combien de pays 


# In[33]:


df_clean['Country'].value_counts() # Nombre de ligne par pays 


# Ce dataset compte 38 pays différents.
# Royaume-Uni = 495 478 lignes soit 91% du total
# On peux filtrer sur certains pays pour mieux explorer l'international, ou nous concentrer uniquement sur UK.

# In[37]:


df['Description'].isna().sum()


# In[ ]:





# In[ ]:





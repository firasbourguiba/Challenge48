# 📌 README - Analyse des Tweets Clients d'Engie

## 📍 **Description du Projet**
Ce projet vise à analyser les tweets adressés au service client d'Engie afin de :
- Nettoyer et structurer les données.
- Effectuer une **analyse de sentiment** (positif, neutre, négatif).
- Identifier les **problèmes clients récurrents**.
- Détecter le **domaine d'activité** de l'entreprise.
- Générer des **indicateurs clés (KPI)** et les visualiser sous forme de graphiques.
- Automatiser l'analyse avec des modèles d'IA (Mistral/Gemini).

## 🛠 **Technologies utilisées**
- **Python** (Pandas, Matplotlib, Seaborn, NLP libraries)
- **Mistral/Gemini** (Analyse de sentiment et catégorisation automatique)
- **Power BI / Streamlit** (Tableaux de bord interactifs)
- **GitHub** (Versioning et collaboration)

## 📂 **Structure du Projet**
```
📁 CHALLENGE_48H
│── 📂 dashboard  # Tableau de bord pour visualisation
│── 📂 data  # Données nettoyées et brutes
│   ├── cleaned_tweets_with_sentiment_updated.csv
│   ├── cleaned_tweets_with_sentiment.csv
│   ├── cleaned_tweets.csv
│   ├── filtered_tweets_engie.csv
│── 📂 models  # Modèles d'IA et de NLP
│   ├── sentiment_model.pkl
│── 📂 notebooks  # Notebooks d'expérimentation
│   ├── sentiment_model_training.ipynb
│── 📂 reports  # Rapports et visualisations
│── 📂 scripts  # Scripts Python pour l'analyse
│   ├── ai_agent.py  # IA pour catégorisation automatique
│   ├── dashboard.py  # Interface de visualisation
│   ├── ID.py  # Correction des IDs en notation scientifique
│   ├── kpi_analysis.py  # Calcul des indicateurs clés
│   ├── preprocess.py  # Prétraitement des données
│   ├── sentiment_analysis.py  # Classification des sentiments
│── .gitignore  # Fichiers à exclure du versioning
│── README.md  # Documentation du projet
```

## 📌 **Étapes Réalisées**

### ✅ **1. Nettoyage des Données**
- Suppression des caractères spéciaux, liens, mentions (@username).
- Conversion des tweets en minuscule.
- Suppression des espaces inutiles et des doublons.
- Correction des IDs pour éviter l'affichage en notation scientifique (**E+23**).

### ✅ **2. Correction des IDs**
- Détection et suppression de la notation scientifique (E+23).
- Conversion des IDs en format numérique lisible.
- Sauvegarde du fichier mis à jour.

### ✅ **3. Analyse des Sentiments**
- Utilisation d'un modèle NLP (Mistral/Gemini) pour classifier les tweets en **Positif, Neutre ou Négatif**.
- Gestion des erreurs API (**429 Too Many Requests**, Timeout).
- Stockage progressif des résultats pour éviter la perte de données.

### ✅ **4. Détection du Domaine de l'Entreprise**
- Extraction des mots les plus fréquents des tweets.
- Classification des tweets en **3 catégories principales** :
  - 🏭 **Énergie** (gaz, électricité, facturation…)
  - 💻 **Technologie** (applications, bugs…)
  - 📞 **Service Client** (réclamations, assistance…)
- Détermination du **secteur dominant** en fonction du volume des plaintes.

### ✅ **5. Génération de KPI et Visualisation**
- Calcul du nombre de tweets par **sentiment** et **secteur**.
- Visualisation des **tendances des plaintes** au fil du temps 📈.
- Création de **graphiques interactifs** avec Power BI ou Streamlit.

## 📊 **Résultats Obtenus**
### 📌 **Classement des tweets par sentiment**
| Sentiment | Nombre de Tweets |
|-----------|-----------------|
| 😊 Positif | 6 tweets |
| 😐 Neutre | 37  tweets |
| 😡 Négatif | 518 tweets |

### 📌 **Classement des tweets par secteur**
| Secteur | Nombre de mentions |
|-----------|-----------------|
| 💻 **Services technologiques** | 31 mentions |
| 📞 **Service client & support** | 329 mentions |

## 🚀 **Prochaines Étapes**
✅ **Intégration des résultats** dans un **tableau de bord interactif** (Power BI, Streamlit).  
✅ **Optimisation des modèles IA** pour affiner la détection des tendances.  
✅ **Mise en place d’un pipeline automatique** pour une analyse en temps réel.

## 🔄 **Comment Exécuter le Projet ?**
1️⃣ **Installer les dépendances** :
```bash
pip install -r requirements.txt
```
2️⃣ **Exécuter le script de nettoyage** :
```bash
python scripts/preprocess.py
```
3️⃣ **Lancer l'analyse des sentiments** :
```bash
python scripts/sentiment_analysis.py
```
4️⃣ **Visualiser les résultats** :
- Ouvrir le fichier **cleaned_tweets_with_sentiment_updated.csv**.
- Consulter les graphiques dans le dossier **reports/**.
- Ouvrir le tableau de bord Streamlit (si utilisé).

---

📌 **Auteur** : Challenge 48h Data Team 🎯
📅 **Date** : Mars 2025


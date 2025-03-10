# Challenge48
Maps 
📂 Challenge_48h_Engie
│── 📂 data                 # 📊 Stockage des fichiers de données brutes et nettoyées
│   ├── filtered_tweets_engie.csv   # Fichier brut contenant les tweets
│   ├── cleaned_tweets.csv         # Fichier nettoyé après traitement
│
│── 📂 scripts              # 📜 Tous les scripts Python du projet
│   ├── preprocess.py       # Script de nettoyage et d'extraction des données
│   ├── kpi_analysis.py     # Script pour calculer les indicateurs KPI
│   ├── sentiment_analysis.py  # Script d'analyse des sentiments
│   ├── ai_agent.py         # Script pour configurer et utiliser les agents IA (Mistral/Gemini)
│   ├── dashboard.py        # Script pour créer le tableau de bord interactif (Power BI ou Streamlit)
│
│── 📂 models               # 🤖 Modèles IA et NLP utilisés
│   ├── sentiment_model.pkl   # Fichier du modèle d'analyse des sentiments (si entraîné localement)
│
│── 📂 notebooks            # 📓 Pour les tests et explorations avec Jupyter Notebook
│   ├── data_exploration.ipynb  # Notebook pour l'exploration et le nettoyage des données
│   ├── sentiment_model_training.ipynb  # Notebook pour entraîner un modèle d'analyse des sentiments
│
│── 📂 reports              # 📑 Résultats et visualisations
│   ├── kpi_report.pdf      # Rapport des KPI analysés
│   ├── sentiment_analysis_results.pdf # Résultats détaillés de l’analyse des sentiments
│
│── 📂 dashboard            # 📊 Fichiers liés au tableau de bord
│   ├── dashboard.pbix      # Fichier Power BI si utilisé
│   ├── streamlit_app.py    # Fichier Streamlit si utilisé
│
│── 📂 config               # ⚙️ Fichiers de configuration (Clés API, paramètres)
│   ├── config.yaml         # Fichier contenant les paramètres du projet (API keys, modèles, etc.)
│
│── 📄 README.md            # 📘 Explication du projet, comment l'exécuter
│── 📄 requirements.txt      # 📜 Liste des packages Python nécessaires (Pandas, NLTK, Streamlit…)
│── 📄 .gitignore           # 🛑 Fichiers à ignorer dans Git (API keys, gros fichiers de data…)
│── 📄 LICENSE              # 📜 Licence du projet (si besoin)

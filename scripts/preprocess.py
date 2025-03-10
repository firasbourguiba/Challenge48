# Script de nettoyage et d'extraction des données
import pandas as pd

import pandas as pd

#  Définition des chemins de fichiers
input_file = "../data/filtered_tweets_engie.csv"
output_file = "../data/cleaned_tweets.csv"

#  Étape 1 : Chargement des données
print(" Chargement des tweets...")
df = pd.read_csv(input_file, sep=";")

# Affichage propre de l'aperçu des données
print("\n Aperçu des premières lignes :")
print(df.head(3))  # jute 3 lignes 

# Vérifier les infos générales du dataset
print("\n Infos sur le dataset avant nettoyage :")
df.info()

#  Étape 2 : Nettoyage des données
df.rename(columns={'full_text': 'tweet_text', 'created_at': 'date', 'id': 'user_id'}, inplace=True)

# Supprimer les tweets venant de "ENGIEpartFR" et "ENGIEgems" dans screen_name
df = df[~df['screen_name'].str.contains("ENGIEpartFR|ENGIEgems", case=False, na=False)]

# Supprimer les lignes avec des valeurs nulles sur des colonnes essentielles
df.dropna(subset=['tweet_text', 'date', 'user_id'], inplace=True)

#  Correction : Conversion de la date avec UTC + gestion erreurs
df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)

# Si des dates n'ont pas pu être converties, on les retire
if df['date'].isnull().sum() > 0:
    print(f"\n Suppression de {df['date'].isnull().sum()} lignes avec date non valide.")
    df.dropna(subset=['date'], inplace=True)

# Convertir user_id en texte et nettoyer
df['user_id'] = df['user_id'].astype(str).str.replace(",", "")

#  Étape 3 : Extraction d'infos utiles
df['hour'] = df['date'].dt.hour
df['tweet_length'] = df['tweet_text'].apply(len)

#  Étape 4 : Évaluation de la criticité des tweets
keywords_urgence = ["panne", "urgence", "scandale", "incident"]
keywords_eleve = ["réclamation", "erreur", "problème"]
keywords_modere = ["facture", "service", "délai"]

def classifier_criticite(tweet):
    text = tweet.lower()
    if any(word in text for word in keywords_urgence):
        return 4  # Urgent
    elif any(word in text for word in keywords_eleve):
        return 3  # Élevé
    elif any(word in text for word in keywords_modere):
        return 2  # Modéré
    else:
        return 1  # Faible

df['criticite'] = df['tweet_text'].apply(classifier_criticite)

#  Garder les doublons, mais sans les tweets ENGIEpartFR ou ENGIEgems
df = df.sort_values(by='date', ascending=False)  # Juste pour l'organisation visuelle

# 📌 Étape 5 : Vérifications finales et export
print("\n Aperçu final des données après suppression des tweets ENGIEpartFR et ENGIEgems :")
print(df[['screen_name', 'tweet_text', 'hour', 'tweet_length', 'criticite']].head(5))

# Sauvegarde des données nettoyées

df.to_csv(output_file, index=False)
print(f"\n Données nettoyées et sauvegardées : {output_file}")

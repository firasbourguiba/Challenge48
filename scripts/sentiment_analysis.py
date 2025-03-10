# Script d'analyse des sentiments
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Charger les tweets nettoyés en forçant l'ID en `str` pour éviter la notation scientifique
tweets_file = "../data/cleaned_tweets.csv"
df = pd.read_csv(tweets_file, dtype={"user_id": str})  # ✅ Charger en string dès le départ

#  Correction : Convertir l'ID en entier pour éviter la notation scientifique
df['user_id'] = df['user_id'].apply(lambda x: str(int(float(x))) if 'E' in x else x)

#  Vérification : Afficher un exemple d'ID après correction
print("Exemple d'ID après conversion :", df['user_id'].head(5))

#  Chargement du modèle d'analyse de sentiment
try:
    print("🔄 Chargement du modèle d'analyse de sentiment (CamemBERT)...")
    sentiment_pipeline = pipeline("text-classification", model="cmarkea/distilcamembert-base-sentiment", tokenizer="camembert-base")
except Exception as e:
    print(f" Erreur avec CamemBERT : {e}")
    print(" Passage à un autre modèle de sentiment en français...")
    sentiment_pipeline = pipeline("text-classification", model="tblard/tf-allocine", tokenizer="tblard/tf-allocine")

#  2. Appliquer le modèle sur chaque tweet et ajouter une colonne "sentiment"
print(" Analyse des sentiments en cours...")
df['sentiment'] = df['tweet_text'].apply(lambda x: sentiment_pipeline(x[:512])[0]['label'])  # Max 512 tokens

# ✅ Correction des labels pour un affichage clair
label_mapping = {
    "LABEL_0": "Négatif 😡",
    "LABEL_1": "Neutre 😐",
    "LABEL_2": "Positif 😊",
    "1 star": "Négatif 😡",
    "2 stars": "Neutre 😐",
    "3 stars": "Neutre 😐",
    "4 stars": "Positif 😊",
    "5 stars": "Positif 😊"
}
df['sentiment'] = df['sentiment'].replace(label_mapping)

#  4. Sauvegarde des résultats avec l'ID corrigé et la colonne "sentiment"
output_file = "../data/cleaned_tweets_with_sentiment.csv"
df.to_csv(output_file, index=False, quoting=1)  #  `quoting=1` empêche Pandas de reformater l'ID

print(f"\n Analyse terminée ! Fichier sauvegardé avec sentiment : {output_file}")

#  5. Visualisation de la répartition des sentiments
sentiment_counts = df['sentiment'].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm", legend=False)
plt.xlabel("Sentiment")
plt.ylabel("Nombre de Tweets")
plt.title("Répartition des Tweets par Sentiment")
plt.show()


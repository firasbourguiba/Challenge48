import pandas as pd
import os

# Définition du chemin du fichier
tweets_file = "../data/cleaned_tweets_with_sentiment.csv"
output_file = "../data/cleaned_tweets_with_sentiment_corrected.csv"

# Vérifier si le fichier existe avant de continuer
if not os.path.exists(tweets_file):
    print(f"❌ Fichier introuvable : {tweets_file}. Vérifie le chemin !")
    exit()

print(f"✅ Fichier trouvé : {tweets_file}")

# Charger le fichier en s'assurant que toutes les colonnes restent des chaînes de caractères
df = pd.read_csv(tweets_file, dtype=str)

# ✅ Correction de la notation scientifique des ID (Conversion brute en chaîne de texte)
df['user_id'] = df['user_id'].apply(lambda x: str(int(float(x))) if 'e' in x else x)

# Vérification des ID après correction
print("\n✅ Exemple d'ID après conversion :")
print(df[['user_id']].head(10))

# Sauvegarde du fichier corrigé en forçant l'ID à rester en texte
df.to_csv(output_file, index=False, quoting=1, encoding="utf-8")

print(f"\n✅ Correction terminée ! Fichier sauvegardé sous : {output_file}")

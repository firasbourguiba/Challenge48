import pandas as pd

# ✅ Charger les tweets annotés
file_path = r"C:\Users\firas\Documents\ynov\B2\challenge 48h\data\cleaned_tweets_with_sentiment.csv"
df = pd.read_csv(file_path, dtype={"user_id": str})  # ✅ Charger les IDs comme texte

# ✅ Correction : Convertir l'ID en entier pour éviter la notation scientifique
df['user_id'] = df['user_id'].apply(lambda x: str(int(float(x))) if 'E' in x else x)

# ✅ Vérifier la correction (afficher les 5 premiers ID)
print(df[['user_id']].head())

# ✅ Sauvegarder le fichier avec les ID correctement formatés
output_file = r"C:\Users\firas\Documents\ynov\B2\challenge 48h\data\cleaned_tweets_with_sentiment_fixed.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Correction des ID terminée ! Fichier sauvegardé sous : {output_file}")

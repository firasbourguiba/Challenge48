import numpy as np

# Convert 'date' to datetime for time-based analysis
df_updated['date'] = pd.to_datetime(df_updated['date'])

# 1. Inconfort moyen
inconfort_moyen = df_updated['Inconfort'].mean()

# 2. Nombre moyen de tweets par utilisateur
tweets_par_utilisateur = df_updated.groupby("user_id").size()
nombre_moyen_tweets_utilisateur = tweets_par_utilisateur.mean()

# 3. Nombre moyen de relance par utilisateur (en supposant que relance = plusieurs tweets d'un même utilisateur)
nombre_moyen_relance_utilisateur = tweets_par_utilisateur[tweets_par_utilisateur > 1].mean()

# 4. Mois avec le plus de tweets négatifs
df_updated['month_year'] = df_updated['date'].dt.to_period('M')
mois_negatif = df_updated[df_updated['Sentiment'] == 'Négatif'].groupby('month_year').size().idxmax()

# 5. Mois avec le plus de tweets positifs
mois_positif = df_updated[df_updated['Sentiment'] == 'Positif'].groupby('month_year').size().idxmax()

# 6. Heure moyenne avec le plus de tweets
df_updated['hour'] = pd.to_datetime(df_updated['Hours'], format='%H:%M:%S').dt.hour
heure_plus_tweets = df_updated.groupby('hour').size().idxmax()

# 7. Temps moyen entre deux tweets d’un même utilisateur
df_updated = df_updated.sort_values(by=['user_id', 'date'])
df_updated['time_diff'] = df_updated.groupby('user_id')['date'].diff()
temps_moyen_entre_tweets = df_updated['time_diff'].mean()

# 8. Sentiment le plus présent selon l’heure
sentiment_par_heure = df_updated.groupby(['hour', 'Sentiment']).size().unstack().idxmax(axis=1)

# 9. Prévision de satisfaction pour 2027 (simple tendance)
df_tendance = df_updated.groupby('month_year')['Inconfort'].mean().reset_index()
df_tendance['month_year'] = df_tendance['month_year'].astype(str)

# 10. Les 5 mots décents les plus utilisés (analyse de texte basique)
from collections import Counter
import re

words = Counter(re.findall(r'\b\w+\b', ' '.join(df_updated['tweet_text'].dropna()).lower()))
mots_decents = words.most_common(5)

# 11. Nombre de tweets moyen par mois
tweets_par_mois = df_updated.groupby('month_year').size().mean()

# 12. Catégories dominantes des tweets
categories_dominantes = df_updated['sentiment_analysis'].value_counts().head(5)

# Résultats
kpi_results = {
    "Inconfort moyen": inconfort_moyen,
    "Nombre moyen de tweets par utilisateur": nombre_moyen_tweets_utilisateur,
    "Nombre moyen de relance par utilisateur": nombre_moyen_relance_utilisateur,
    "Mois avec le plus de tweets négatifs": str(mois_negatif),
    "Mois avec le plus de tweets positifs": str(mois_positif),
    "Heure avec le plus de tweets": heure_plus_tweets,
    "Temps moyen entre deux tweets d'un même utilisateur": temps_moyen_entre_tweets,
    "Sentiment le plus fréquent par heure": sentiment_par_heure.to_dict(),
    "5 mots décents les plus utilisés": mots_decents,
    "Nombre moyen de tweets par mois": tweets_par_mois,
    "Catégories dominantes des tweets": categories_dominantes.to_dict()
}

# Affichage des résultats
import ace_tools as tools
kpi_df = pd.DataFrame(list(kpi_results.items()), columns=["KPI", "Value"])
tools.display_dataframe_to_user(name="KPIs Analysis", dataframe=kpi_df)

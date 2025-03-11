import numpy as np
import statsmodels.api as sm

# Préparation des données pour la prévision
df_updated['year_month'] = df_updated['date'].dt.to_period('M')
negative_tweets_per_month = df_updated[df_updated['Sentiment'] == 'Négatif'].groupby('year_month').size()

# Convertir en DataFrame pour la modélisation
df_forecast = negative_tweets_per_month.reset_index()
df_forecast.columns = ['year_month', 'negative_tweet_count']
df_forecast['year_month'] = df_forecast['year_month'].astype(str)  # Conversion pour éviter les erreurs

# Convertir les dates en valeurs numériques (mois successifs)
df_forecast['month_number'] = np.arange(len(df_forecast))

# Modélisation avec une régression linéaire
X = sm.add_constant(df_forecast['month_number'])
y = df_forecast['negative_tweet_count']
model = sm.OLS(y, X).fit()

# Prédire pour 2027 (ajout de nouveaux mois)
future_months = np.arange(len(df_forecast), len(df_forecast) + 12*3)  # Prédiction jusqu'en décembre 2027
X_future = sm.add_constant(future_months)
predicted_negative_tweets = model.predict(X_future)

# Création d'un DataFrame pour afficher les prédictions
future_dates = pd.date_range(start="2025-01-01", periods=len(future_months), freq='M').to_period('M')
df_predictions = pd.DataFrame({"year_month": future_dates.astype(str), "predicted_negative_tweets": predicted_negative_tweets})

# Affichage des résultats
import ace_tools as tools
tools.display_dataframe_to_user(name="Prévision Tweets Négatifs 2027", dataframe=df_predictions)

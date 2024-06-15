import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Charger les données
csv_file = 'data/file.csv'
data = pd.read_csv(csv_file)

# Sélection des caractéristiques et de la cible
X = data[['moyenne_degre_var', 'ratio_clauses_sur_vars', 'positive_literals_percentage', 'avg_literals_per_clause']]
y = data['difficulte']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=22)

# Entraîner le modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitude globale : {accuracy}")

# Sauvegarder le modèle
modele_file = 'modele/logistic_model.pkl'
with open(modele_file, 'wb') as f:
    pickle.dump(model, f)

print(f"Modèle sauvegardé dans {modele_file}")













# Entraîner le modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Sauvegarder le modèle
with open('logistic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

CNF Difficulty Predictor
Description
Le CNF Difficulty Predictor est un outil qui permet de prédire la difficulté des instances CNF en utilisant un modèle de régression logistique. L'outil utilise une interface graphique pour permettre aux utilisateurs de charger des fichiers CNF, calculer diverses métriques, et afficher la difficulté prédite de l'instance CNF.

Installation



Clonez le dépôt :

git clone https://github.com/FoualMo/CNF-instances-difficulty-prediction.git



cd cnf-difficulty-predictor

Assurez-vous que le fichier logistic_model.pkl est présent dans le répertoire principal. Ce fichier contient le modèle de régression logistique entraîné.

Utilisation
Ligne de commande
Vous pouvez utiliser l'outil directement en ligne de commande pour prédire la difficulté d'une instance CNF :

python predict_cnf_difficulty.py path/to/your/cnf/file.cnf



Interface Graphique
Pour une utilisation plus conviviale, vous pouvez lancer l'interface graphique :




Lancer l'interface graphique :
python interface.py
Utilisation de l'interface graphique :
Cliquez sur le bouton "Ouvrir un fichier CNF" pour charger votre fichier CNF.
Les métriques de l'instance CNF et la difficulté prédite seront affichées dans la fenêtre.

import tkinter as tk
from tkinter import filedialog
import pickle
import numpy as np
from pysat.formula import CNF

# Charger le modèle à partir du fichier
model_file = 'logistic_model.pkl'
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Fonctions auxiliaires pour calculer les métriques
def average_variable_degree(cnf):
    variable_counts = {}
    for clause in cnf.clauses:
        for literal in clause:
            var = abs(literal)
            if var in variable_counts:
                variable_counts[var] += 1
            else:
                variable_counts[var] = 1
    total_degrees = sum(variable_counts.values())
    num_variables = len(variable_counts)
    average_degree = total_degrees / num_variables if num_variables > 0 else 0
    return average_degree

def positive_literal_frequency(cnf):
    total_literals = sum(len(clause) for clause in cnf.clauses)
    positive_literals = sum(sum(1 for lit in clause if lit > 0) for clause in cnf.clauses)
    return positive_literals / total_literals if total_literals > 0 else 0

def average_literals_per_clause(cnf):
    total_literals = sum(len(clause) for clause in cnf.clauses)
    num_clauses = len(cnf.clauses)
    avg_literals_per_clause = total_literals / num_clauses if num_clauses > 0 else 0
    return avg_literals_per_clause

def ratio_clauses_vars(cnf):
    return len(cnf.clauses) / len(set(abs(lit) for clause in cnf.clauses for lit in clause))

def predict_difficulty(model, cnf):
    avg_var_deg = average_variable_degree(cnf)
    pos_lit_freq = positive_literal_frequency(cnf)
    ratio_clauses_vars_value = ratio_clauses_vars(cnf)
    avg_literals_clause = average_literals_per_clause(cnf)
    
    instance_features = np.array([[avg_var_deg, ratio_clauses_vars_value, pos_lit_freq, avg_literals_clause]])
    difficulty = model.predict(instance_features)
    return difficulty[0], avg_var_deg, ratio_clauses_vars_value, pos_lit_freq, avg_literals_clause

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CNF files", "*.cnf"), ("All files", "*.*")])
    if file_path:
        cnf = CNF(from_file=file_path)
        difficulty, avg_var_deg, ratio_clauses_vars_value, pos_lit_freq, avg_literals_clause = predict_difficulty(model, cnf)
        difficulty_str = {0: "Difficile", 1: "Facile", 2: "Inconnu"}[difficulty]
        
        result = f"""
        Détails de l'instance CNF :

        - Degré moyen des variables : {avg_var_deg:.2f}
        - Ratio clauses/variables : {ratio_clauses_vars_value:.2f}
        - Pourcentage des littéraux positifs : {pos_lit_freq*100:.2f}%
        - Nombre moyen de littéraux par clause : {avg_literals_clause:.1f}
        - Prédiction de difficulté : {difficulty_str}
        """
        result_label.config(text=result)

# Interface graphique
root = tk.Tk()
root.title("Prédiction de la difficulté des instances CNF")

frame = tk.Frame(root)
frame.pack(pady=20)

btn_open = tk.Button(frame, text="Ouvrir un fichier CNF", command=open_file)
btn_open.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=20)

root.mainloop()

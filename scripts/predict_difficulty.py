import sys
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from pysat.formula import CNF

# Fonction pour prédire la difficulté d'une nouvelle instance CNF
import pickle

import numpy as np


def predict_difficulty(model, cnf):
    avg_var_deg = average_variable_degree(cnf)
    pos_lit_freq = positive_literal_frequency(cnf)
    ratio_clauses_vars = len(cnf.clauses) / len(set(abs(lit) for clause in cnf.clauses for lit in clause))
    avg_literals_clause = average_literals_per_clause(cnf)
    
    instance_features = np.array([[avg_var_deg, ratio_clauses_vars, pos_lit_freq, avg_literals_clause]])
    difficulty = model.predict(instance_features)
    return difficulty[0]

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
    avg_literals_clause = total_literals / num_clauses if num_clauses > 0 else 0
    return avg_literals_clause



# Charger le modèle à partir d'un fichier
def load_model(model_file):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    return model


def main():
    if len(sys.argv) != 3:
        print("Usage: python predict_difficulty.py <model_file> <cnf_file>")
        sys.exit(1)
    
    model_file = sys.argv[1]
    cnf_file = sys.argv[2]
    

    # Charger le modèle
    model = load_model(model_file)
    
    # Charger l'instance CNF
    cnf = CNF(from_file=cnf_file)
    
    # Prédire la difficulté
    difficulty = predict_difficulty(model, cnf)
    difficulty_str = {0: "Difficile", 1: "Facile", 2: "Inconnu"}[difficulty]
    print(f"La difficulté de l'instance est : {difficulty_str}")

if __name__ == "__main__":
    main()

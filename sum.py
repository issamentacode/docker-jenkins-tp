import sys

def additionner(arg1, arg2):
    """
    Additionne deux nombres et retourne le résultat.

    :param arg1: Premier nombre à additionner (float)
    :param arg2: Deuxième nombre à additionner (float)
    :return: La somme de arg1 et arg2 (float)
    """
    return arg1 + arg2

# Vérifier si deux arguments sont fournis
if len(sys.argv) != 3:
    print("Erreur : Deux arguments sont nécessaires.")
    sys.exit(1)

# Interpréter les arguments
try:
    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])
except ValueError:
    print("Erreur : Les arguments doivent être des nombres.")
    sys.exit(1)

# Calculer la somme
resultat = arg1 + arg2

# Afficher le résultat
print(resultat)

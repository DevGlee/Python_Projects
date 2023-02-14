import numpy as np

#On crée une nouvelle liste en kg
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45] 

#On crée une autre en numpy a partir de la première
np_weight_kg = np.array(weight_kg)

#On crée une variable pour convertir les kg en pounds
np_weight_lbs = np_weight_kg * 2.2

#On affiche
print(np_weight_lbs)

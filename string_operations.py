astr = "Bonjour Billy"

print("le nombre de caractères est :")
print(len(astr))     #Compte le nombre de caractère dans la chaines

print("La position de i est ",astr.index("i"))  #Affiche la position d'un caractère dans la chaine

print(astr.count("B"))   # Compte le nombre de fois que le caractère est présent dans la chaine

print(astr[2:6])         #Affiche les caractères présent dans l'intervalle

print(astr[1:3:7])        #ici on saute un caractère dans l'intervalle il s'agit du septième
print(astr[1:6])
print(astr[1:6:1])        # on saute le premier caractère

print(astr[::-1])         # Inverser la chaine de caractère


print(astr.upper())   # On met la chaine de caractère en majuscule
print(astr.lower())   #  "" minuscule

print(astr.startswith("Bonjour"))      # Fonction boolean determinant si la chaine commence avec le string indiqué
print(astr.endswith("Broly"))


import re   #On importe le module re

find_members = []                  #On intialise la variable
for member in dir(re):              # On parcours le module
    if "find" in member:
        find_members.append(member)  #Chaque fonction contenant find on les selectionne
   
print(sorted(find_members))  #On affiche
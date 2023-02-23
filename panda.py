import pandas as pan


#On initialise le dictionnaire
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}



brics = pan.DataFrame(dict) #On utilise une fonction de pandas nommé DataFrame pour ainsi modélisé un tableau


#La fonction Index  permet de changer les clés des pays en lettre

brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)                #Affichage

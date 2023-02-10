class Mclass:
    variable = "hello"
    variable2 = "how are you"

    def function(self):
        print("Messagee de la fonction")


class NumberHolder:
    def __init__(self, number):  # On defini le ou les attributs
        self.number = number     # On l'initialise

    def returnNumber(self):
        return self.number  # Ici on defini la fonction returnNumber qui retournera le nombre


# Ici la variable sera egale à la fonction NumberHolder qui contient le nombre 10
var1 = NumberHolder(10)

# ainsi on print la variable avec la fonction qui retourne les nombres
print(var1.returnNumber())

myobjectz = Mclass()  # myobjectz obtiendra la variable présente dans la class
myobjecty = Mclass()  # "" ""  "" "" "" "" "" " " " " " " " """  ""

myobjectz.variable = "salut"
print(myobjectz.variable)
myobjectz.function()

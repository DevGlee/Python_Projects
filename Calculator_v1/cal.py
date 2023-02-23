####### SIMPLE CALCULATRICE V1 #######

#La fonction va additionner les deux variables
def addition(x,y):
    return x+y

#La fonction va soustraire les deux variables
def soustraction(x,y):
    return x-y

#La fonction va multiplier les deux variables
def multiplication(x,y):
    return x*y

#La fonction va diviser les deux variables
def division(x,y):
    return x/y


print("Selectionner l'operation")

print("Addition")

print("Soustraction")

print("Multiplication")

print("Division")

while True:
    #Choix de l'opération
    choix = input("Entrer votre choix 1/ 2/ 3/ 4")
    
    #Gestion des choix
    
    if choix in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Entrer votre premier nombre: '))
            num2 = float(input("Entrer votre deuxième nombre: "))
        except ValueError:
            print("Entrée invalide, s'il vous plaît entrer vos nombres")
            continue
        if choix == '1':
            print (num1, "+", num2, "=", addition(num1, num2))
        elif choix == '2':
            print (num1, "-", num2, "=", soustraction(num1, num2))
        elif choix == '3':
            print (num1, "x", num2, "=", multiplication(num1, num2) )
        elif choix == '4':
            print (num1, '/', num2, "=", division(num1, num2))
        
        prochain_calcul = input ("Voulez-vous effectuer un autre calcul ? oui / non")
        if prochain_calcul == "non":
            break
else:
    print ("Entrée invalide")
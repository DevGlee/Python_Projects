
# On défini les fonctions par le préfixe 'def' suivi des parenthèses qui peuvent accepter des paramètres

def hl():
    print("Hello from function")


def hl_args(username, greeting):
    print("Hello %s , from my function , i wish you %s " %
          (username, greeting))


def sum_two_num(a, b):
    return a + b

# Appeller les fonctions


hl()

hl_args("Billy", "An Happy New Year")

x = sum_two_num(1+3)


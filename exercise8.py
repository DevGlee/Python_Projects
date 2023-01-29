# Utiliser 3 fonctions pour concatener des chaines de carractère


# Fonction pour la liste

def list_benefits():
    return ['More organized code', 'More readable code', 'Easier code reuse', 'Allowing programmers to share and connect code together']


# Fonction pour les chaines présentes dans la liste qui sera concatener avec un bout de phrase
def build_sentence(benefit):
    return "%s is a benefit of functions" % benefit

# Fonction pour utiliser les 3 en meme temps


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:  # Parcours la liste
        print(build_sentence(benefit))        # Affiche les chaines de caractère concatener avec le bout de phrase

name_the_benefits_of_functions()

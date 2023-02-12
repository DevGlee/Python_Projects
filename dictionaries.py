phonebook = {}

phonebook['Billy'] =  6901234567
phonebook['Paul'] = 6909876548

#Supprimer une valeur   
# del phonebook['Billy']  ou  phonebook.pop('Billy')

print(phonebook)

#Alternative pour initialiser
#phonebook ={
#     'Billy' = 6901234567,
#     'Paul' =  6909876548
# }

#Parcourir le dictonnaire

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
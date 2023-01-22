#################  CONDITIONS   ###############

f = 24

print(f==24)
print(f==48)
print(f<96)


name = "bijoul"
age = 23

if name == "bijoul" and age == 23:
    print("Your name is bijoul, and you are also 23 years old")

if name == "bijoul" or name == "zouti" :
    print("Your name is either bijoul or zouti")

if name in ["bijoul", "zouti"] :
    print("Your name is either bijoul or zouti")



statement = True
another_statement = False

if statement is True:
    print("Statement is true")
    pass
elif another_statement is True:
    print("Another Statement is True")
    pass
else:
    print("False")
    pass

i = 6

if i == 6:
    print("i est égale à six")
else:
    print("i n'est pas égale à six")


u = [1,2,3]
p = [1,2,3]

print(u == p)
print(u is p)

print(not False)
print((not False) == (False))
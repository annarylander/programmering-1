# Kontrollera datatyp
grade = "A"
year = "2022"
last_year = '2022'
is_registred = True
is_not_registred = False
month = 3
temperature = 20.5
test = None

print(type(grade))
print(type(year))
print(type(last_year))
print(type(is_registred))
print(type(is_not_registred))
print(type(month))
print(type(temperature))
print(type(test))


# Skillnad på int och str när vi summerar
x = "10"
y = "10"

print(x + y)

a = 10
b = 10

print(a + b)


#Ändra datatyp
int(x)
str(a)


# Lägga ihop strängar
name = "Anna"
last_name = "Rylander"
year = 2022

print("Hej " + name + " " + last_name + " " + str(year))

# Booleans
a = 20
b = 20

print(a == b) 


#Facit övningar

#1
grade = "A" #str
year = "2022" #str
last_year = '2022' #str
is_registred = True #bool
is_not_registred = False #bool
month = 3 #int
temperature = 20.5 #float
test = None #None

#2
favorite_color = "gul"
print("Min favoritfärg är " + favorite_color)

#3
cups_coffe = 3
print("Jag drack " + str(cups_coffe) + " koppar kaffe idag")

#4.1
name = "Anna"
favorite_food = "pasta"
print(name)
print(favorite_food)

#4.2
print("Jag heter " + name)
print("Min favoritmat är " + favorite_food)

#4.3
print("Jag heter " + name + " och min favoritmat är " + favorite_food)

#4.4
age_ = 32
print("Jag heter " + name + " och är " + str(age_))


#5
a = 5
b = 2
print(a == b) #False

c = 30
d = "30"
print(c == d) #False

e = "50"
f = '50'
print(e == f) #True

g = 5
h = 5
print(g == h) #True

i = 0
j = None
print(i == j)  #False

k = 0
x = False
print(k == x) #True

#extra
current_year = 2022
birth_year = 1990
age = current_year - birth_year

print("Du är " + str(age))







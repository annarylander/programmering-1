# Artimetska operatorer +-*/ // %
print(8 + 2)

print(8 - 2)

print(8 * 2)

print(8 / 2)

print(8 // 2)

print (8 % 2)


# Jämförelseoperatorer ==, !=, >, <, >=, <=
print(8 == 2)

print(8 != 2)

print(8 > 2)

print(8 < 2)

print(8 >= 2)

print( 8 <= 2)



# If, else, elif exempel
weather = "sunny"

if weather == "rainy":
  print("Bring an umbrella")



hungry = True

if hungry:
  print("feed me")


a = 33
b = 200

if b > a:
  print("b är större än a")
elif a == b:
  print("a är lika med b")
else:
  print("a är större än b")


age = 19

if age < 13:
		print("Är ett barn")
elif age > 12 and age <= 19:
		print("Är en tonåring")
else: 
		print("Är vuxen")


#Övning 1
brand = "Audi"
model_year = 2000
model = "A3"
current_mileage = 8000
big_service_mileage = 6000


print("You own a " + brand, model + " that has been driven for " + str(current_mileage))

#samma sak men enklare:
print(f"You own a {brand} {model} that has been driven for {current_mileage}")

if current_mileage > big_service_mileage:
    print("Time for big service")

#Övning2
age = 12

if age > 18:
    print("Du får rösta i valet")
else:
    print("Du får inte rösta än")

#Övning3
x = 0

if x > 0:
    print("x är ett positivt tal")
elif x < 0:
    print("x är ett negativt tal")
elif x == 0:
    print("x är lika med 0")


#Övning4
temperature = 15

if temperature <10:
    print("Det är kallt, ta med en jacka")
elif temperature >20:
    print("Du behöver ingen jacka idag")

#Övning 5
points = 50

if points >= 80 and points <= 90:
  print("Betyg A")
elif points >= 70 and points < 80:
  print("Betyg B")
elif points >= 60 and points < 70:
  print("Betyg C")
elif points >= 50 and points < 60:
  print("Betyg D")
elif points >= 40 and points < 50:
  print("Betyg E")
elif points == 0 and points < 40:
  print("Betyg F")


#Övning 6
y = 4

if y % 2 == 0:
  print("y är ett jämn tal")
else:
  print("y är ett ojämnt tal")
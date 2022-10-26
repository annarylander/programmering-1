#Datatyper
name= "John"
age = 25
points = 2.5
is_fun = True
x = None

#Detta är olika variabler
age = 30
Age = 30

#Få ut id
print(id(age))

# Ta reda på datatyp
print(type(age))
print(type(name))
print(type(points))
print(type(is_fun))
print(type(x))

#Ändra datatyp
x = 0
print(bool(x))


#Strängar
print("Jag heter " + name)
print(f"Jag heter {name}")
print("Här är en stäng och \nen till på ny rad")


#Aritmetiska operatorer
1 + 1
2 - 1
1 * 2
2 / 2
2 // 2
10 % 2


#Tilldelning
this_year = 2022
this_year = this_year + 1
this_year += 1
this_year -= 1
print(this_year)

#Jämförelse
x = 10
y = 20
z = 30

print(z == x)
print(z > x)
print(y < x)
print(z <= x)

#Logiska
print(y > x and y < z)
print(y > x or y < z)

#Villkor

exempel = "Den här skolan heter Jensen gymnasium"

if "Jensen" in exempel:
  print("Jensen fanns i meningen")
elif "komvux" in exempel:
  print("komvux finns i meningen")
else:
  print("Finns inte")


#Funktioner

def multiply(num1, num2):
  result = num1 * num2
  return result

def add(num1, num2):
  result = num1 + num2
  return result
  
x = multiply(2, 5)
y = multiply(2, 10)
z = multiply(2, 20)
c = multiply(2, 30)
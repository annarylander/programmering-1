#Gruppuppgift
shopping_cart = [25, 100, 49, 250, 549, 38, 499, 799]

sum = 0

for price in shopping_cart:
  if price > 100:
    price = price * 0.9
  sum = sum + price

print(f"Du har handlat för {sum} kr")


#1
for n in range(5, 21):
  print(n)

#2
animals = ["cat", "dog", "panda", "mouse", "fox", "bear" ]

for animal in animals:
  print(animal)

#3
names = ["John", "Alice", "Ali", "Charlie", "Emma", "Samira"]

for name in names:
  print("Welcome " + name)

#4
programming1 = "Python"

for letter in programming1:
  print(letter)

#5
city= "Stockholm"
c=0

for letter in city:
  c += 1
print(c)

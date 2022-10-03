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


#6
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]

for name in lst1:
  lst2.append(f"dr {name}")

print(lst2)

#7.1
for n in range(2, 21, 2):
  print(n)

#7.2
for i in range(1, 21):
  if i % 2 == 0:
    print(i)


#8
lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]

for number in lst1:
  lst2.append(number *2)

print(lst2)


#9
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]

for number in lst1:
  if number > 0:
    lst2.append(number)

print(lst2)






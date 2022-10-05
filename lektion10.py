#1 med while
counter = 0
total = 0

while counter <= 100:
    total= total+counter 
    counter= counter+1
print(total)

#1 med for
sum = 0

for i in range(101):
  sum += i

print(sum)


#2 med while
num = int(input("Skriv en siffra: "))
count = 1

while count <= 10:
    multiplied = count * num
    count += 1
    print(f"{num} x {count} = {multiplied}")
    

#2 med for
number = int(input("Skriv in en siffra: "))

for count in range(1, 11):
    multiplied = number * count
    print(number, "x", count, "=", multiplied)

#3
fruits = ["Apples", "Oranges", "Chips", "Grapes", "Pears", "Sallad"]

for fruit in fruits:
    if fruit == "Milk" or fruit == "Sallad":
        continue
    print(fruit)
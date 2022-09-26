#Genomgång Listor

food = ["bread", "milk", "egg", "apples", "coffee"]


# Lägga till sist
food.append("chips")

print(food)


# Lägga till på en indexposition
food.insert(1, "cake")

print(food)


# Ta bort
food.remove("egg")

print(food)

# Ta bort på indexposition
food.pop(1)

print(food)


# Sortera
food.sort()

print(food)

#Rensa en lista
food.clear()

print(food)


x = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(x[2][1])


#Dictionary
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

print(person["last_name"])

person["phone"] = "555-555-5555"

print(person)
#1
def greeting(greeting, name):
    print(f"{greeting} {name}")

greeting("Hej", "Anna")

#2
def greeting(greeting, name="stranger"):
    print(f"{greeting} {name}")

greeting("Hej")


#3
def multiply(num1, num2):
    sum = num1 * num2
    return sum

multiply(2, 5)

#4
def isPositive(num):
    if num > 0:
        return True
    else:
        return False

isPositive(-5)

#5
def isAdult(age):
    if age >= 18:
        print("Du får rösta")
    else:
        print("Du får inte rösta")

isAdult(2)

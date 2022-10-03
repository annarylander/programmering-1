#Gruppuppgift
secret_numb = 9

count = 0

while count < 3:
    guess = int(input("Guess: "))
    count += 1
    if guess == secret_numb:
        print("Grattis du vann!")
        break
else: print("Du förlorade")



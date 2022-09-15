#1
name = input("Vad heter du? ")
print("Hej " + name)

town = input("Var bor du? ")
print("Du bor i " + town)

work = input("Var jobbar du? ")
print("Du jobbar på " + work)

print(f"Du heter alltså {name} och bor i {town} och jobbar på {work} ")



#2
name = input("Please enter your name.")
if name == "Bond":
    print("Welcome on board 007.")
else:
    print("Good morning " + name)


#3
day = input("Vilken dag är det?: ").lower()

if day == "måndag":
    print("Det dag 1")
elif day == "tisdag":
    print("Det är dag 2")
elif day == "onsdag":
    print("Det är dag 3")
elif day == "torsdag":
    print("Det är dag 4")
elif day == "fredag":
    print("Det är dag 5")
elif day == "lördag":
    print("Det är dag 6")
elif day == "söndag":
    print("Det är dag 7")


#4
name = input("Vad heter du? ")
print(len(name))








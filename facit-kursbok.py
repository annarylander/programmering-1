# Facit till övningsuppgifterna i kursboken 

# Datatyper

#3.1
i = 47

#3.2
x = 67.5

#3.3
namn = "Det är kul med Python"

#3.4
a = 42.0
print("talet är " + str(a))

#3.5
l = [4, 6, 32]

#3.6
# nej namet kan inte börja med siffra

#3.7
flagga = True

#3.8
l[2] = 42


#3.9
l = ["a", 2, 7, 3.0, 4.5]

print(l[-1])


#3.10
tom_lista = []

#3.11
l2 = l[1:]
print(l2)

#3.12
l2 = l[1:-1]
print(l2)

#3.13
l.append(100)

#3.14
l.insert(0, 52)

#3.15
l.insert(2, -27)


#3.16
names = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
names.remove("Per")

#3.17
del names[1]


# #3.18
del names[3:]

#3.19
del names[0:2]

#3.20
spread_sheet = []

spread_sheet.append([42] * 6)
spread_sheet.append([42] * 6)
spread_sheet.append([42] * 6)
spread_sheet.append([42] * 6)
spread_sheet.append([42] * 6)

print(spread_sheet[2][2])

#3.21

telefon_bok = {
    "Arne" : "47",
    "Bengt": "91",
    "Stina": "19",
    "Lena": "98"
}

#3.22 
print("Stina" in telefon_bok)
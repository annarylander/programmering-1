#Exempel set/list
import time


# Skapa en lista siffror
l = [i for i in range(0, 90000000)]
print(len(l))


# Skapa ett set med samma siffror
s = set()
for i in range(0, 90000000):
    s.add(i)
print(len(s))


# nummer som ska testas om de finns i lista/set
test_numbers = [0, 128, -3999, 90000, 1022, 1, 1.21212, 3.14]


# sök i lista
start_time = time.time()

for t in test_numbers:
    if t in l:
        print(f'yes, {t} exists in list')

end_time = time.time()
print(end_time - start_time)


# sök i set
start_time = time.time()
for t in test_numbers:
    if t in s:
        print(f'yes, {t} exists in set')

end_time = time.time()
print(end_time - start_time)


import random

def play():
    user = input("Vad väljer du? 'sten' 'sax' eller 'påse'\n")
    computer = random.choice(['sten', 'sax', 'påse'])
    print(f"Du valde {user}, datorn valde {computer}")

    if user == computer:
        return "Oavgjort!"

    if is_win(user, computer):
        return "Du vann!"

    return "Du förlorade!"

def is_win(player, opponent):
    if (player == "sten" and opponent == "sax") or (player == "sax" and opponent == "påse") \
        or (player == 'påse' and opponent == 'sten'):
        return True

print(play())
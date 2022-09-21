print("Välkommen till swish-beräknaren")
bill = float(input("Hur mycket var notan på? SEK"))
tip = int(input("Hur många procent vill ni ge i dricks? 10, 12, or 15? "))
people = int(input("Hur många ska dela på notan?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Varje person ska betala: {final_amount} SEK")

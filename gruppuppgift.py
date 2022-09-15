#lösningsförslag gruppuppgift v.2

cost_per_cup = 20
discount_amount = 1000

number_cups = 40 
has_discount = False

amount_spent = number_cups * cost_per_cup

has_discount = amount_spent >= discount_amount 

if has_discount: 
    print(f"Du har rätt till rabatt eftersom du har köpt {number_cups} koppar och spenderat {amount_spent}")
else:
    cups_until_discount = (discount_amount - amount_spent) / cost_per_cup
    print(f"Du måste köpa {cups_until_discount} koppar innan du har rätt till rabatten")

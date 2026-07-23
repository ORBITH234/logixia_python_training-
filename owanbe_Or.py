
can_transfer = False

user_choice = input("please indicate if you have cash or not (y/n)? ").upper()

has_cash = user_choice == "Y"

if has_cash or can_transfer:
    print("Thank you for your patronage! Take your charger.")
else:
    print("Ah, no money? Please drop my market.")
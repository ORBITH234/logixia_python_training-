print("The Busisness Rules(Prices)")
bill = 0
vehicle = input("are you driving a (Sedan , SUV) ? ").upper()
if vehicle == "SEDAN":
  bill = 1500
else:
  bill = 2500
  
vacuum = input("do you want the interior vacuumed (Y/N)? ").upper()
if vacuum == "Y":
  bill += 500
  
engine = input("do you want an engine wash (Y/N)? ").upper()
if engine == "Y":
  bill += 1000
print(f"your final bill is ₦{bill}")
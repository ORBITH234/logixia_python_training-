print("Welcome To Base Suya Size")

suya_price = 0

suya_size = input("What size of Suya do you want ?(S,M,L) ").upper()
if suya_size == "S":
  suya_price = 1500
elif suya_size == "M":
  suya_price = 2000
else:
  suya_price = 2500

Onion_Cabbage = input("Do you want extra onions and cabbage ?(Y/N)").upper()
if Onion_Cabbage == "Y":
  if suya_size == "S":
      suya_price = suya_price + 200
  else:
        suya_price += 300
  
pepper = input("Do you want pepper ? (Y/N)").upper()
if pepper == "Y":
   suya_price += 100
print(f"your final bill is: ₦{suya_price }")

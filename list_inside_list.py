import random
regular_guests = ["Tunde", "Ngozi", "Emeka"]
vip_guests = ["Davido", "Wizkid", "Burna Boy"]

wedding_seats = [regular_guests, vip_guests]
target_guest = random.choice(vip_guests[1:])
print(f"Please escort {target_guest} to the high table!")
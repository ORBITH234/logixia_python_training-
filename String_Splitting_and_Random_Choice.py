import random

# 1. The long string from the conductor
conductor_shout = "Oshodi, Mushin, Ojuelegba, Fadeyi"

# 2. Converting the String into a List
bus_stops = conductor_shout.split(", ")

print(bus_stops)
# Output: ['Oshodi', 'Mushin', 'Ojuelegba', 'Fadeyi']

# 3. The Shortcut: Picking a random item directly
random_stop = random.choice(bus_stops)
print(f"I think I will drop at {random_stop}.")
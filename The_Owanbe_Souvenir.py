# The Owanbe Souvenir

# The Business Requirement: You are the chief planner for a Lagos Owambe. You have a massive sack of random souvenirs, and as guests leave, you reach in and give them one randomly.

# The Steps:

# 1 Start with this exact list: souvenirs = ["Plastic Basin", "Wall Clock", "Customized Jotter", "Umbrella", "Hand Fan"]
# 2 You have a VIP guest leaving. Using the random.choice() shortcut, select a random souvenir from the list.
# 3 Print exactly: "Thank you for coming! Here is your [Souvenir]."


import random
souvenirs = ["Plastic Basin", "Wall Clock", "Customized Jotter", "Umbrella", "Hand Fan"]
vip = random.choice(souvenirs)
print(f"Thank you for coming! Here is your {vip}.")
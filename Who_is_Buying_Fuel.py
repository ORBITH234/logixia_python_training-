# task

# The Business Requirement:
# The estate transformer just blew up, and there is no NEPA light. You and
#  your flatmates need to turn on the generator, but nobody wants to pay 
# for the fuel. Write a program that asks for everyone's names and 
# randomly selects someone to buy the fuel.
# Rule: For this specific challenge, 
# you are NOT allowed to use random.choice(). 
# You must use random.randint() and 
# list indexing to prove you understand the math behind it!)



import random
user = input("enter the names of the tenanat here: \n").capitalize()
all_user = user.split(",")
new_user = random.randint(0,len(all_user)-1)
chosen_tennant = all_user[new_user]
print(chosen_tennant)

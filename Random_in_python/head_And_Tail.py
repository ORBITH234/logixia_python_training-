# Rice Coin Toss

# It is Sunday afternoon. You and your siblings have just finished a massive pot of Sunday Jollof rice, and now there is a mountain of plates in the sink. Nobody wants to wash them. You decide to settle it the fair way: a virtual coin toss!

# The Business Requirement: Write a program that acts as a virtual coin toss. Every time the program is run, it must randomly output one of two exact phrases:

#     "Heads"
#     "Tails"

import random
toss = random.choice(["HEAD","TAIL"])
print(toss)
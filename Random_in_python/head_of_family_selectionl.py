# chosing the the head of the family 

# The Business Requirement: Write a program that acts as a virtual selection . Every time the program is run, it must randomly output one of four exact phrases:
# "father","Mother","senior-brother","Junior_sister"
#and always give success if its sellected father as the head of the family
import random
family = ["father","Mother","senior-brother","Junior_sister"]
family = random.choice(family)
if family == "father":
    print(f"success ,{family} is the head of the family")
else :
    print(f"{family} is not the head of the family")
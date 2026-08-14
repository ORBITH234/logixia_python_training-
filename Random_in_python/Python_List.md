# Python List

The Concept: Up until now, every time we wanted to store a piece of data in our code, we created a single variable. Think of a variable like a single box.

If you were building a program to store ingredients for Sunday Jollof Rice, using normal variables would look like this:

## python
item1 = "Tomatoes"
item2 = "Tatashe"
item3 = "Onions"
item4 = "Maggi"
item5 = "Bay Leaves"

Imagine if you had 50 items! Writing 50 different variables would be an absolute nightmare. Your code would be huge, messy, and prone to errors. We need a way to group related data together inside a single container. To do this, Python gives us a Data Structure called a List.

The Naija Analogy (The Mile 12 Market List): When you go to Mile 12 market, you don't write your ingredients on 50 tiny, separate pieces of paper and stuff them into different pockets (which is what individual variables are). You bring out one long piece of paper, and you write all the items together in a specific sequence.

In Python, the square brackets [ ] act as the edges of that piece of paper. Inside those brackets, you write your items.

But how do you pull an item out of the list? We use something called an Index (the position of the item). But here is a massive trap for beginners: Computers do not start counting at 1. They start counting at 0.

Why? Think of the index as an "offset"—how many steps away from the start are you?

    "Tomatoes" is at the very beginning. You take 0 steps to reach it. So, its index is 0.
    "Tatashe" is 1 step away from the start. So, its index is 1.

This is called Zero-Indexing, and it is a fundamental rule of programming!

Code Example:

python
# Creating our list
jollof_ingredients = ["Tomatoes", "Tatashe", "Onions", "Maggi", "Bay Leaves"]

# Pulling items out using their index
first_item = jollof_ingredients[0]
print(f"The first thing we need to buy is {first_item}.")

third_item = jollof_ingredients[2]
print(f"Don't forget the {third_item}!")

# Code Breakdown:

    The Brackets []: When Python sees square brackets on the right side of an equals sign, it immediately knows, "Ah, we are creating a List!"
    The Comma ,: Every individual item inside the list must be separated by a comma. If you forget the comma, Python will crash.
    The Index [0]: When we want to grab a specific item, we write the name of the list, followed immediately by square brackets containing the index number. jollof_ingredients[0] reaches into the list and pulls out the string "Tomatoes". jollof_ingredients[2] pulls out "Onions".

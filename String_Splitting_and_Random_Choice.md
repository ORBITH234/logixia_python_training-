# String Splitting and Random ChoiceThe Concept:
 Sometimes, you won't have the luxury of typing out a beautiful, perfectly formatted Python List yourself. Sometimes, data comes to you as one long string of text, and you need to convert it into a List so you can work with it. We do this using a built-in Python method called .split().

We are also going to look at a shortcut. In Part 2, you used random.randint() along with the length of a list to pick a random item. Python actually has a built-in cheat code inside the random module just for this, called random.choice().

The Naija Analogy (The Danfo Conductor): Imagine you are at the bus stop, and a Danfo conductor is shouting the route: "Oshodi, Mushin, Ojuelegba, Fadeyi!"

Right now, that is just one long sentence (a String). But if you want to count the stops or pick one randomly, you need to separate them. The .split() method is like you telling the conductor to pause at every comma and write each stop on a separate line of a piece of paper (a List). You tell Python exactly what character to look for to make the split—usually a comma and a space ", ".


# Code Breakdown:

    .split(", "): This method looks at your string, searches for every instance of a comma followed by a space, cuts the string at those exact points, and places the resulting pieces into a brand new List.
    random.choice(list_name): Instead of calculating the length of the list and using randint to find a random index, random.choice() reaches directly into your list and pulls out a random item for you. It saves you so much time!


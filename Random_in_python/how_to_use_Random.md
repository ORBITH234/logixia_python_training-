## Concept Reading
# andom

Welcome to module 6! You have officially survived the logic mazes of module 5, and now we are stepping into a whole new world. Up until now, our code has been deterministic—it does the exact same thing every single time you run it. But to build games, pick random winners, or shuffle data, we need to make our code unpredictable.

The Concept:
To generate random numbers, we need to use a "Module". Python is a massive language with thousands of built-in tools. But if Python loaded every single tool into your computer's memory every time you ran a simple print() statement, your computer would be terribly slow!

To fix this, Python keeps most of its tools packed away in separate storage boxes called Modules. When you need a specific tool—like the one that generates random numbers—you have to explicitly tell Python to go fetch it before you can use it. We do this using the import keyword. Today, we are using the random module, and specifically a function inside it called randint(a, b) which gives us a random whole number between a and b (inclusive).

The Naija Analogy (The Store Room):
Imagine you are living in a flat in Surulere, and you need to pound yam for Sunday lunch. You don't keep your heavy wooden mortar and pestle sitting in the middle of your living room all day! It lives in the kitchen store room.

When it is time to pound the yam, you walk to the store and bring it out. In Python, your code file is the kitchen. Typing import random at the very top of your file is you saying: "Abeg Python, go to the store room and bring me the 'random' tool. I need it right now!"

Once you have brought the tool into the kitchen, you can use it to do things like rolling a virtual dice for a heated game of Ludo under the mango tree!


# Final Project: Escape to Murtala Muhammed Airport (Treasure Island Naija Remix)

<!-- The Scenario: You have a 10:00 PM British Airways flight to London from Murtala Muhammed Airport (MMA). It is 6:00 PM on a Friday in Lagos, and the rain just started pouring. Your mission is to build a game where the player must make the exact right sequence of choices to navigate the chaos of Lagos, avoid the Agberos, and make it to their gate. One wrong move, and they miss their flight!

The Business Requirements (Game Logic):

    The Welcome: The program must first print a welcome message: "Welcome to Lagos! Your mission is to survive the traffic and catch your flight."
    Crossroad 1 (The Transport):

    Prompt the user: "You step out of your gate. Do you take an 'Okada' or a 'Danfo'? "
    If they choose "danfo", they survive and move to the next level.
    If they choose "okada" (or literally anything else), output: "Taskforce arrests your Okada on the highway. Game Over." and the game ends.

    Crossroad 2 (The Breakdown):

    Prompt the user: "The Danfo breaks down at Oshodi. Do you 'Wait' for the conductor to fix it, or 'Walk' across the bridge? "
    If they choose "wait", they survive and move to the final level.
    If they choose "walk" (or anything else), output: "Agberos corner you and collect your transport fare. Game Over." and the game ends.

    Crossroad 3 (The Terminal Doors):

    Prompt the user: "You finally run into the airport. There are three terminal doors: 'Red', 'Yellow', or 'Green'. Which do you choose? "
    If they choose "green", output: "You breeze through check-in, grab a meat pie, and board your flight to London! YOU WIN!"
    If they choose "red", output: "Wahala! Customs officers hold you back to check your bags for dried fish. You miss your flight. Game Over."
    If they choose "yellow", output: "A fake ticketing agent scams you and gives you a boarding pass for a luxury bus to Onitsha. Game Over."
    If they type anything else at all, output: "You got confused, missed your way, and the plane left you. Game Over." -->

## Crucial Technical Requirement: Users are unpredictable! Your game MUST be case-insensitive. If a user types "DANFO", "Danfo", or "danfo", the game must treat it all as correct. You must handle this dynamically.

# Your Task: Use nested if, elif, and else statements to build out this exact game logic. Remember, if a player dies at Crossroad 1, they should never see the question for Crossroad 2!
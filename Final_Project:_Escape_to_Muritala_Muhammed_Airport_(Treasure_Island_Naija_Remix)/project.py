print("Welcome to Lagos! Your mission is to survive the traffic and catch your flight.")

transport = input("You step out of your gate. Do you take an 'Okada' or a 'Danfo'? ").lower()

if transport == "danfo":
    breakdown = input(
        "The Danfo breaks down at Oshodi. Do you 'Wait' for the conductor to fix it, "
        "or 'Walk' across the bridge? "
    ).lower()

    if breakdown == "wait":
        door = input(
            "You finally run into the airport. There are three terminal doors: "
            "'Red', 'Yellow', or 'Green'. Which do you choose? "
        ).lower()

        if door == "green":
            print(
                "You breeze through check-in, grab a meat pie, and board your flight "
                "to London! YOU WIN!"
            )
        elif door == "red":
            print(
                "Wahala! Customs officers hold you back to check your bags for dried "
                "fish. You miss your flight. Game Over."
            )
        elif door == "yellow":
            print(
                "A fake ticketing agent scams you and gives you a boarding pass for "
                "a luxury bus to Onitsha. Game Over."
            )
        else:
            print(
                "You got confused, missed your way, and the plane left you. Game Over."
            )

    else:
        print("Agberos corner you and collect your transport fare. Game Over.")

else:
    print("Taskforce arrests your Okada on the highway. Game Over.")
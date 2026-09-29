from config import choices
from game import determine_winner
from difficulty import get_computer_choice
from validation import check_choice
from score import score
from history import add_history, show_history


print("===== ROCK PAPER SCISSORS =====")

print("\nChoose Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Enter your choice: ")

if difficulty == "1":
    difficulty = "Easy"
elif difficulty == "2":
    difficulty = "Medium"
elif difficulty == "3":
    difficulty = "Hard"
else:
    difficulty = "Easy"

print("Difficulty:", difficulty)

rounds = int(input("\nEnter number of rounds: "))

for i in range(rounds):

    print("\nRound", i + 1)

    player_choice = input(
        "Enter rock, paper, or scissors: "
    ).lower()

    while not check_choice(player_choice, choices):
        print("Invalid choice!")
        player_choice = input(
            "Please enter rock, paper, or scissors: "
        ).lower()

    computer_choice = get_computer_choice(
        player_choice,
        difficulty,
        choices
    )

    result = determine_winner(
        player_choice,
        computer_choice
    )

    print("Your choice:", player_choice)
    print("Computer choice:", computer_choice)
    print("Result:", result)

    if result == "player wins":
        score["wins"] += 1
    elif result == "computer wins":
        score["losses"] += 1
    else:
        score["draws"] += 1

    add_history(
        player_choice,
        computer_choice,
        result
    )


print("\n===== FINAL SCORE =====")
print("Wins:", score["wins"])
print("Losses:", score["losses"])
print("Draws:", score["draws"])

show_history()
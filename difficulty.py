import random

def get_computer_choice(player_choice, difficulty, choices):

    if difficulty == "Easy":
        return random.choice(choices)

    elif difficulty == "Medium":
        if random.random() < 0.5:
            return random.choice(choices)
        else:
            if player_choice == "rock":
                return "paper"
            elif player_choice == "paper":
                return "scissors"
            else:
                return "rock"

    elif difficulty == "Hard":
        if player_choice == "rock":
            return "paper"
        elif player_choice == "paper":
            return "scissors"
        else:
            return "rock"
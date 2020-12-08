import random
import os


def messages(winner):
    msg = {
        "Rock": "Rock crushes scissors",
        "Paper": "Paper covers rock",
        "Scissors": "Scissors cuts paper",
    }
    return msg.get(winner)


# Determine who is the winner
def play(computer, user):
    if computer == user:
        return "A Draw Play Again", "No One"
    if computer == "Rock" and user == "Scissors":
        return messages(computer), "Computer"
    elif computer == "Paper" and user == "Rock":
        return messages(computer), "Computer"
    elif computer == "Scissors" and user == "Paper":
        return messages(computer), "Computer"
    else:
        return messages(user), "You"


def main():
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    computer_hand = random.choice(list(choices.values()))

    # clear console (teminal) screen before starting th game
    os.system("cls") if os.name == "nt" else os.system("clear")
    for index, choice in choices.items():
        print(f"[{index}] {choice}")

    response = input("Choose your hand: ")
    user_hand = choices.get(response)

    msg, winner = play(computer_hand, user_hand)
    print("-" * 20)
    print(f"{winner} Win\n{msg}")


if __name__ == "__main__":
    main()
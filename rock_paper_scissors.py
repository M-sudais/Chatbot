import random

def play_game():
    options = ("rock", "paper", "scissors", "cancel")
    options2 = ("rock", "paper", "scissors")
    while True:
        player = None
        bot = random.choice(options2)
        while player not in options:
            player = input("Enter one of the options ('rock, paper or scissors') or ('cancel') to leave: ")
        if player.lower() == "cancel":
            print("Goodbye then...")
            break
        else:
            print(f"Player: {player}")
            print(f"Bot: {bot}")
        if player == bot:
            print("It's a Draw!")
        elif player == "rock" and bot == "scissors":
            print("You win!")
        elif player == "paper" and bot == "rock":
            print("You win!")
        elif player == "scissors" and bot == "paper":
            print("You win!")
        else:
            print("You lose!")
        play_again = input("Do you want to play again?(y/n): ")
        if play_again != "y":
            print("Thanks for playing!")
            break

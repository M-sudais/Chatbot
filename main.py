# PUT THE COIN TOSS GAME HERE SINCE I WAS HAVING TROUBLING IMPORTING THE FILE FOR SOME REASON
def play_gamee():
    print("Welcome to the coin toss game!")
    print("Pick your sides!")
    sides = input("Who wants to pick first? (A/B) ").lower()
    if sides == 'a':
        Ateam = input("Okay Team A! Heads or tails? (H/T) ").lower()
        if Ateam == 'h':
            Bteam = 't'
            h = "team A"
            t = "team B"        
            print("Okay Team B, looks like you're tails.")
        elif Ateam == 't':
            Bteam = 'h'
            h = "team B"
            t = "team A"
            print("Okay Team B, looks like you're heads.")
        else:
            print("Invalid answer.") 
    elif sides == 'b':
        Bteam = input("Okay Team B! Heads or tails? (H/T) ").lower()
        if Bteam == 'h':
            Ateam = 't'
            h = "team B"
            t = "team A"
            print("Okay Team A, looks like you're tails.")
        elif Bteam == 't':
            Ateam = 'h'
            h = "team A"
            t = "team B"
            print("Okay Team A, looks like you're heads.")
        else:
            print("Invalid answer.")
    else:
        print("Invalid answer!")
    listy = [h, t]
    print(" ")
    answer = input("Time to toss the coin! are you ready? (Y/N)").lower()
    import random
    if answer == 'y':
        toss = random.choice(listy)
        print(f"Congratulations {toss}, you win the coin toss!")
    else:
        print("Goodbye then...")

#MAIN CODE STARTS HERE
import datetime #IMPORTS THE DATETIME MODULE
import chatbotdictionaries #IMPORTS THE FILE WHERE THE DICTIONARY FOR THE CHATBOT IS
from difflib import get_close_matches
import rock_paper_scissors #IMPORTS THE ROCK PAPER SCISSORS GAME I MADE IN A SEPERATE FILE
import generate_password #IMPORTS THE GENERATE PASSWORD CODE THAT WAS MADE IN A SEPERATE FILE

#MAKING THE DATE AND TIME FUNCTION HERE SINCE I HAD TROUBLE IMPORTING THE FILE FOR SOME REASON
def format_date_time():
    now = datetime.datetime.now()

    # FORMAT DATE AS "MONDAY, 23RD SEPTEMBER 2024"
    date_str = now.strftime("%A, %d %B %Y")
    day_suffix = "th" if 11 <= now.day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(now.day % 10, 'th')
    formatted_date = date_str.replace(f"{now.day:02}", f"{now.day}{day_suffix}")

    # FORMAT TIME AS 9:24AM"
    formatted_time = now.strftime("%I:%M%p").lower()

    return formatted_date, formatted_time

#THE MAIN CODE BEGINS HERE
def main():
    print("Welcome to Group 4's amazing chatbot system!")
    while True: #THIS ENSURE THE CODE ALWAYS LOOPS BACK TO THE INPUT STATEMENT BELOW UNLESS BROKEN BY THE "EXIT" WORD
        user_input = input("You're now speaking to the chatbot! (If you want to leave, simply type 'exit'): ").strip()

        if "exit" in user_input.lower(): #ENSURES THAT NO MATTER WHAT IS TYPED, IF EXIT IS IN IT, THE LOOP WILL BREAK AND THE CODE WILL END
            print("so you really want to go?? goodbye then!")
            break

        if "a game" in user_input.lower(): #ENSURES THAT NO MATTER WHAT YOU TYPE, AS LONG AS "A GAME" IS INCLUDED, THE CODE BELOW WILL BE CARRIED OUT
            game = input("Enter a number to pick a game: 1 ='rock,paper,scissors', 2 ='coin toss', 3 ='cancel': ")
            if game == "1":
                rock_paper_scissors.play_game()
                continue
            elif game == "2":
                play_gamee()
                continue
            elif game == "3":
                continue
            else:
                print("Invalid response, try again.")
                continue


        if "date" in user_input.lower(): #ENSURES THAT NO MATTER WHAT IS TYPED, IF "DATE" IS IN THAT SENTENCE, THE CODE WILL TELL YOU THE DATE
            formatted_date, _ = format_date_time()
            print(f"The current date is: {formatted_date}")
            continue
        elif "time" in user_input.lower(): #ENSURES THAT NO MATTER WHAT IS TYPED, IF "TIME" IS IN THAT SENTENCE, THE CODE WILL TELL YOU THE TIME
            _, formatted_time = format_date_time()
            print(f"The current time is: {formatted_time}")
            continue

        if "password" in user_input.lower(): #ENSURES THAT NO MATTER WHAT IS TYPED, IF "PASSWORD" IS IN THAT SENTENCE, THE CODE WILL GENERATE A PASSWORD
            generate_password.password()
            continue 

        matches = get_close_matches(user_input, chatbotdictionaries.chatbot.keys(), n=1, cutoff=0.6)
        if matches:
            response = chatbotdictionaries.chatbot[matches[0]]
            if callable(response):
                print(response())
            else:
                print(response)
        else:
            print("I do not have any knowledge on the subject matter")



if __name__ == "__main__":
    main()

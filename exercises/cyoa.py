"""Choose Your Own Adventure Game."""

__author__ = "730548773"

points: int
player: str = ""
WAVING_EMOJI: str = "\U0001F44B"
STOP_EMOJI: str = "\U0001F6D1"
SAD_EMOJI: str = "\U0001F625"
GIGGLE_EMOJI: str = "\U0001F92D"
THUMBS_UP: str = "\U0001F44D"
THUMBS_DOWN: str = "\U0001F44E"
THINKING_EMOJI: str = "\U0001F914"
CLAPPING_EMOJI: str = "\U0001F44F"
CONFETTI_EMOJI: str = "\U0001F389"


def main() -> None:
    """Entrypoint of the game."""
    global points
    global player
    points = 0
    greet()
    first_choice: int = int(input(f"Okay, {player}, nice to meet you {WAVING_EMOJI}! Would you like to 1: play the whole game, 2: just play the number-guessing portion, or 3: quit? "))
    while first_choice < 1 or first_choice > 3:
        first_choice = int(input(f"{STOP_EMOJI} That's not a valid option! Please try again: "))
    if first_choice == 1:
        points = starting_number(points)
        prediction()
    if first_choice == 2:
        points = starting_number(points)
    if first_choice == 3:
        print(f"{SAD_EMOJI} Aw, it was nice to meet you! Bye! {WAVING_EMOJI}")
        quit()
    keep_playing: bool = True
    while keep_playing is True:
        loop_choice: int = int(input((f"Okay {player}, currently you have {points} points! Would you like to 1: reset your points, start over, and play the whole game again, 2: play just the second stage with your current number of points, or 3: stop playing? ")))
        while loop_choice < 1 or loop_choice > 3:
            loop_choice = int(input(f"{STOP_EMOJI} That's not a valid option! Please try again: "))
        if loop_choice == 1:
            points = 0
            points = starting_number(points)
            prediction()
        if loop_choice == 2:
            prediction()
        if loop_choice == 3:
            keep_playing = False
            print(f"Thank you for playing {GIGGLE_EMOJI}! You are ending this game with {points} points.")
          
  
def greet() -> None:
    """Greets the player and establishes their name."""
    print(f"Hello {WAVING_EMOJI}! Welcome to my game.")
    global player
    player = input("What is your name? ")


def starting_number(points: int) -> int:
    """First stage of the game in which the player guesses the number."""
    from random import randint
    print(f"Okay, {player}. In the first stage of this game, you must guess a number correctly. Based on the number of times it takes you to guess the number, you will have good {THUMBS_UP} or bad {THUMBS_DOWN} luck in the second stage of the game!")
    secret: int = randint(1, 20)
    guess: int = int(input(f"I am thinking of a number from 1-20. What number am I thinking of? {THINKING_EMOJI}"))
    while guess != secret:
        if guess > secret:
            guess = int(input("Unfortunately, your guess is too high! Please guess again: "))
            points += 1
        elif guess < secret:
            guess = int(input("Unfortunately, your guess is too low! Please guess again: "))
            points += 1
    if guess == secret:
        print(f"Yayyy!!! You got it! {CLAPPING_EMOJI}")
    return points


def prediction() -> None:
    """Second stage of the game in which the player answers a series of riddles/questions."""
    global points
    global player
    print(f"Okay, {player}, in the second stage of the game, please reply with the number specifying the answer choice you wish to select. The lower your points, the better {THUMBS_UP}!")
    if points <= 5:
        if points != 1:
            print(f"Since you have only {points} points, consider yourself lucky {GIGGLE_EMOJI}! You will receive easy riddles. Every time you guess correctly, your points value ({points}) will decrease, and vice versa.")
        else:
            print(f"Since you have only {points} point, consider yourself lucky {GIGGLE_EMOJI}! You will receive easy riddles. Every time you guess correctly, your points value ({points}) will decrease, and vice versa.")
        easy_riddle_one: int = int(input("Here is the first riddle. I start with M, end with X, and have a never-ending amount of letters. What am I? 1: Mix, 2: Mailbox, 3: Multiplex, or 4: Matrix: "))
        while easy_riddle_one < 1 or easy_riddle_one > 4:
            easy_riddle_one = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if easy_riddle_one == 2:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")
        easy_riddle_two: int = int(input("Here is the second riddle. I am a 7-letter word. I become longer when my third letter is removed. Who am I? 1: Lounger, 2: Longing, 3: Lengthy, or 4: Longine: "))
        while easy_riddle_two < 1 or easy_riddle_two > 4:
            easy_riddle_two = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if easy_riddle_two == 1:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")
        easy_riddle_three: int = int(input("Okay, here is the final riddle! Kris's mother had four kids: Bladee, Ecco2K, ThaiBoy Digital, and... 1: Yung Lean, 2: Lucki, 3: Summrs, or 4: Kris: "))
        while easy_riddle_three < 1 or easy_riddle_three > 4:
            easy_riddle_three = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if easy_riddle_three == 4:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")
    else:
        print(f"Oh no! Since you have so many points ({points}), you will be unlucky {SAD_EMOJI}. This stage of the game will give you some very difficult trivia questions. Every time you guess correctly, your points value ({points}) will decrease, and vice versa.")
        hard_riddle_one: int = int(input("Here is the first question. What United States state has more people than all of Canada? 1: California, 2: Texas, 3: New York, or 4: North Carolina: "))
        while hard_riddle_one < 1 or hard_riddle_one > 4:
            hard_riddle_one = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if hard_riddle_one == 1:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")
        hard_riddle_two: int = int(input("Here is the second question. How long was the shortest war in history? 1: 3 hours, 2: 45 minutes, 3: 38 minutes, 4: 2 days and 1 hour: "))
        while hard_riddle_two < 1 or hard_riddle_two > 4:
            hard_riddle_two = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if hard_riddle_two == 3:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")
        hard_riddle_three: int = int(input("Okay, here is the final question! What percent of their buried food do squirrels lose to thieves? 1: 25% 2: 50% 3: 15% 4: 75%: "))
        while hard_riddle_three < 1 or hard_riddle_three > 4:
            hard_riddle_three = int(input(f"{STOP_EMOJI} Oops, that is not an option! Please try again: "))
        if hard_riddle_three == 1:
            points -= 1
            print(f"Congratulations {CONFETTI_EMOJI}! You got it right.")
        else:
            points += 1
            print(f"Unfortunately, that is not the right answer {SAD_EMOJI}.")


if __name__ == "__main__":
    main()

"""EX02- One shot Wordle."""

__author__ = "730548773"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
character_count: int = 0
guess_emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if len(guess) == len(secret):
    while character_count < len(secret):
        if guess[character_count] == secret[character_count]:
            guess_emoji += GREEN_BOX
        else:
            checking: bool = False
            alt_index: int = 0
            while checking == False and character_count < len(secret) and alt_index < len(secret):
                if guess[character_count] == secret[alt_index]:
                    checking = True
                else:
                    alt_index = alt_index + 1
            if checking == True:
                guess_emoji += YELLOW_BOX
            else:
                guess_emoji += WHITE_BOX
        character_count += 1
else:
    length: bool = False
    while len(guess) != len(secret) and length == False:
        guess = input(f"That was not {len(secret)} letters! Try again: ")    
        if len(guess) == len(secret):
            length: bool = True
            while character_count < len(secret):
                if guess[character_count] == secret[character_count]:
                    guess_emoji += GREEN_BOX
                else:
                    checking: bool = False
                    alt_index: int = 0
                    while checking == False and character_count < len(secret) and alt_index < len(secret):
                        if guess[character_count] == secret[alt_index]:
                            checking = True
                        else:
                            alt_index += 1
                    if checking == True:
                        guess_emoji += YELLOW_BOX
                    else:
                        guess_emoji += WHITE_BOX
                character_count += 1

print(guess_emoji)

if guess == secret:
    print("Woo! You got it!")
    exit()
else:
    print("Not quite. Play again soon!")
    exit()
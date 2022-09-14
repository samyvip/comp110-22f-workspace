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
    """Checks whether the length of the guess matches the length of the secret word."""
    while character_count < len(secret):
        if guess[character_count] == secret[character_count]:
            guess_emoji += GREEN_BOX
            """Prints a green box if the the letter at the current index of the guessed word matches the letter at the same index of the secret word."""
        else:
            checking: bool = False
            alt_index: int = 0
            while checking is False and character_count < len(secret) and alt_index < len(secret):
                if guess[character_count] == secret[alt_index]:
                    checking = True
                else:
                    alt_index = alt_index + 1
            if checking is True:
                guess_emoji += YELLOW_BOX
                """Prints a yellow box if the letter at that index of the guessed word is in the secret word, but not in the same position."""
            else:
                guess_emoji += WHITE_BOX
                """Prints a white box if the letter at that index of the guessed word is not present at any index in the secret word."""
        character_count += 1
else:
    length: bool = False
    while len(guess) != len(secret) and length is False:
        guess = input(f"That was not {len(secret)} letters! Try again: ") 
        """Prompts the user to re-enter a word of the appropriate length."""   
        if len(guess) == len(secret):
            length = True
            while character_count < len(secret):
                if guess[character_count] == secret[character_count]:
                    guess_emoji += GREEN_BOX
                    """Prints a green box if the the letter at the current index of the guessed word matches the letter at the same index of the secret word."""
                else:
                    checking = False
                    alt_index = 0
                    while checking is False and character_count < len(secret) and alt_index < len(secret):
                        if guess[character_count] == secret[alt_index]:
                            checking = True
                        else:
                            alt_index += 1
                    if checking is True:
                        guess_emoji += YELLOW_BOX
                        """Prints a yellow box if the letter at that index of the guessed word is in the secret word, but not in the same position."""
                    else:
                        guess_emoji += WHITE_BOX
                        """Prints a white box if the letter at that index of the guessed word is not present at any index in the secret word."""
                character_count += 1

print(guess_emoji)
"""Prints resulting emoji string."""

if guess == secret:
    """Checks whether user has guessed the word correctly."""
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
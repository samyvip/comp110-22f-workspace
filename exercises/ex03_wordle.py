"""EX03- Wordle."""

__author__ = "730548773"

WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
GREEN_BOX: str = "\U0001F7E9"


def contains_char(word: str, character: str) -> bool:
    """Searches for character."""
    assert len(character) == 1
    checking: bool = False
    word_index: int = 0
    while checking is False and word_index < len(word):
        if character == word[word_index]:
            checking = True
        else:
            word_index = word_index + 1
    if checking is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Calls contains_char fn to test for colored box codification."""
    assert len(guess) == len(secret)
    guess_emoji: str = ""
    word_index: int = 0
    while word_index < len(guess):
        if guess[word_index] == secret[word_index]:
            guess_emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[word_index]):
                guess_emoji += YELLOW_BOX
            else:
                guess_emoji += WHITE_BOX
        word_index += 1
    return guess_emoji


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    success: bool = False
    while turns <= 6 and success is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            success = True
        else:
            turns += 1
    if guess == secret:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main
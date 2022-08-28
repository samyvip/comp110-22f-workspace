"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730548773"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

character_count: int = 0

print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]:
    character_count = character_count + 1
    print(single_character + " found at index 0")
    

if single_character == five_character_word[1]:
    character_count = character_count + 1
    print(single_character + " found at index 1")

    
if single_character == five_character_word[2]:
    character_count = character_count + 1
    print(single_character + " found at index 2")
    
   
if single_character == five_character_word[3]:
    character_count = character_count + 1
    print(single_character + " found at index 3")
    

if single_character == five_character_word[4]:
    character_count = character_count + 1
    print(single_character + " found at index 4")

   
if int(character_count) >= 2:
    print(str(character_count) + " instances of " + str(single_character) + " found in " + str(five_character_word))  

if int(character_count) < 2:
    if int(character_count) == 0:
        print("No instances of " + str(single_character) + " found in " + str(five_character_word))
    else:
        print(str(character_count) + " instance of " + str(single_character) + " found in " + str(five_character_word))

import random

hangman_words = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
attempts = 6
with open("weekend.txt", mode="r") as file:
    data = file.read()
    words = data.split()
    for word in words:
        hangman_words.append(word)
        
hangman_word = random.choice(hangman_words)
reveal = {}
for char in hangman_word:
        reveal[char] = False
while attempts > 0:
    print(f"You have {attempts} attempts remaining")
    for char in hangman_word:
        if reveal[char]:
            print(f"{char}", end="")
        else:
            print("_", end=" ")
    print(f"\nAvailable letters: \n{letters}")
    char_guess = input("Guess a letter:")[0]
    char_guess = char_guess.lower()
    if char_guess.isalpha() == False:
        print("Enter a letter")
        continue
    letters.remove(char_guess)
    print(f"Your guess: {char_guess}")
    if char_guess in hangman_word:
        reveal[char_guess] = True
    else:
        attempts -= 1
        
    if False not in reveal.values():
        print("You Win!!")
        print(f"The word is: {hangman_word}")
        break
if attempts == 0:
    print("You Lose!!")    
    print(f"The word is: {hangman_word}")
import random

name = input("what is your name:")
print("good luck!", name)

#list os possible words:

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# select a random word
word = random.choice(words)

print("\nguess the characters")

#stores the guesses characters
guesses = ''
turns = 12

# main game loop

while turns > 0:

    failed = 0

    # display guessed characters and hidden letters
    for char in word:
        if char in guesses:
            print(char, end="")
        
        else:
            print("_", end="")
            failed +=1
    print()

    #check if the word has been guessed
    if failed == 0:
        print("you won")
        print("the word is:", word)
        break
    #get user input
    guess = input("guess a character:").lower()

    #validate input length
    if len(guess) != 1:
        print("please enter a single character.")
        continue
    #check for duplicate guesses
    if guess in guesses:
        print("you already guessed that character.")
        continue

    #store the guess
    guesses += guess

    #handle incorrect guesses
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", turns, "more guesses")

        #check if user has lost
        if turns ==0:
            print("you lost.")
            print("the word was:", word)



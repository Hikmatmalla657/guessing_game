import random

print(f"welcome!\nthis is nbr guessing_game. let's start.")

low = int(input("enter low number:"))
high = int(input("enter high number:"))



print(f"select number between {low} and {high}. Let's start")

num = random.randint(low, high)

# chance give
ch = 7
#guesing 
gh = 0

while gh < ch:
    gh += 1
    guess = int(input("enter you guessing number:"))

    if guess == num:
        print(f"correct the num is {num}. the guess is in {ch} attepmt.")

        break
    elif gh >= ch and guess != num:
    
        print(f"sorry the number was {num}. better luck next time!")

    elif guess > num:
        print("too high! try lower number.")

    elif guess < num:
        print("'too low! try higher number.")
        
    
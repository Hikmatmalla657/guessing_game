import random

print(f"welcome! this is the guessing game. \n you have 7 chances to complete. let's start:")

low = int(input("enter the low bound:"))
high = int(input("enter the high bound:"))

print(f"you have 7 chances to complete between {low} and {high} numbers.")

num = random.randint(low, high)

#allowed chance
ch = 7

#guessing
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("enter your guess:"))

    if guess == num:
        print(f"correct! you have completed is {num}. you guessed it in {gc} attempt.")
        break

    elif gc >= ch and guess != num:
        print(f"sorry! you missed out.")
    
    elif gc > ch:
        print("too high. choose lower number.")
    
    elif gc < ch:
        print("too low. choose higher number.")

    


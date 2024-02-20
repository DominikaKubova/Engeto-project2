##Bulls & Cows game --> looking for the correct 4 digit number 

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Dominika Kubová
email: dominika.kubova@kbc.com
discord: dominika_50263
"""


import random
import sys 

SEPARATOR = 30 * "="

def bulls_cows_count(guess, number):
    bull_cow = [0,0] 
    guess_list = [i for i in str(guess)]
    number_list = [i for i in str(number)]
    
    for digit_guess, digit_number in zip(guess_list, number_list):
        if digit_guess in number_list:
            if digit_guess == digit_number:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    print("BULLS = ", bull_cow[0], "/ COWS = ", bull_cow[1])    
    


## MAIN CODE ##
print(SEPARATOR)
print("Welcome to the game - Bulls & Cows!")
print(SEPARATOR)
print("I have generated a random 4-digit number for you.\nLet's play!.")

#Generation of random 4-digit number which does not start with 0
number = str(random.randint(1000 , 9999))
#print(number)

print(SEPARATOR)



#Program will notify if the quessed number is not 4-digit long, will be duplicated, starting with 0 or will not be integer

guessed_numbers = []
guess = 0

while guess != number:   
    if len(guessed_numbers) % 5 == 0 and guess != 0:
        decision = input("Do you want to reveal guessed number? If yes, answer \"YES\", if you want to keep trying just hit enter!")
        if decision == "YES":
            print(number)
            sys.exit()
        else:
            print("OK, keep trying!") 

    guess = input("Enter a 4-digit number: ")
    if guess.isnumeric() and int(guess) in range(1000 , 9999):
        if guess not in guessed_numbers:
            guess_analyses = bulls_cows_count(guess, number)
            guessed_numbers.append(guess)
        else:
            print("You have already tried this number.")
    else:
        print("The inserted guess is not in a valid format! Please check if you used 4-digit number.")
        continue



print("Congratulations, the number", guess, "is the correct guess! You won in", len(guessed_numbers), "attempts.")

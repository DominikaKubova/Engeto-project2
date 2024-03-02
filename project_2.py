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

def introduction():
    """Prints a welcome massage and informs the palyer that the random number is generated"""
    print(SEPARATOR)
    print("Welcome to the game - Bulls & Cows!")
    print(SEPARATOR)
    print("I have generated a random 4-digit number for you.\nLet's play!.")    

def random_number() -> str:
    """Generates random 4 digit number with no duplicities"""
    number = str(random.randint(1000 , 9999))
    while len(set(number)) != 4: 
    #print(number)
        number = str(random.randint(1000,9999))
    return(number)     

def hint(number: str, guessed_numbers: list):
    """
    Every 5 valid guesses player is asked if wants to contitnue or the randon number is reveled.

    Keyword arguments:
    guess -- input from the player
    guessed_numbers -- list of already used valid guesses
    """
    if len(guessed_numbers) % 5 == 0 and len(guessed_numbers) != 0:
        message_hint = "Do you want to reveal guessed number?\n"\
                        "If yes, answer \"YES\","\
                        " if you want to keep trying just hit enter!"
        decision = input(message_hint)
        if decision == "YES":
            print(number)
            sys.exit()
        else:
            print("OK, keep trying!")

def player_guess_check(guess: str) -> bool:
    """
    Checks the input from the player. If the format is not correct, message assigned to the problem is shown.
    If the format is correct game continues. Function returns True if the format is correct, otherwise False.

    Keyword arguments:
    guess -- input from the player
    """
    guess_list = [i for i in guess]
    if guess_list[0] == "0":
        print("The 4-digit number can not start with 0.")
        return False
    if not guess.isdigit(): 
        print("The inserted guess is not in a valid format!")
        return False
    if len(guess) != 4 and guess.isdigit():
        digits_of_guess = len(guess)
        print("The number has to contain 4-digits. Your guess conatins", digits_of_guess, "digits.")   
        return False
    return True     

def player_guess_valid(number: str, guess: str, guessed_numbers: list):
    """If player's guess is in valid format, check if the guess has already been tried,
    if not, adds the guess to list of guesses
    
    Keyword arguments:
    number -- random number generated
    guess -- input from the player
    guessed_numbers -- list of already used valid guesses
    """
    if guess not in guessed_numbers:
        bulls_cows_count(guess, number)
        guessed_numbers.append(guess)
    else:
        print("You have already tried this number.")
     
def bulls_cows_count(guess: str, number: str):
    """
    Counting bulls and cows from guessed number.

    Keyword arguments:
    guess -- input from the player
    number -- random number generated
    """
    bull_cow = [0,0] 
    guess_list = [i for i in guess] 
    number_list = [i for i in number]
    
    for digit_guess, digit_number in zip(guess_list, number_list):
        if digit_guess in number_list:
            if digit_guess == digit_number:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    print("BULLS = ", bull_cow[0], "/ COWS = ", bull_cow[1])    
    
def game():
    """
    Process of the game: introtuction of the play, generating random number, validating 
    the player's guess with bulls and cows counter until the guess is equal to number.
    """
    introduction()
    number = random_number()
    print(SEPARATOR)
    #print(type(number))

    guessed_numbers = []
    guess = 0
    #guess = None

    while guess != number: 
        hint(number, guessed_numbers)    
        guess = input("Enter a 4-digit number: ")
    
        if not player_guess_check(guess):
            continue
        player_guess_valid(number, guess, guessed_numbers)
        
    print("Congratulations, the number", guess, "is the correct guess! You won in", len(guessed_numbers), "attempts.")

## MAIN CODE ##
if __name__ == "__main__":
    game()
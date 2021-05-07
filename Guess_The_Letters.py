# This program will generate a random word with
# the help of RandomWordGenerator module and
# ask the user to guess the word.

from RandomWordGenerator import RandomWord # Install from pip
import datetime # Install from pip

# This function will greet the user according to the current time.
def greeting():
    print("*****\nWELCOME TO THE GUESS THE NUMBER GAME\n*****")
    name = input('Enter your name here:- ')

    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        print(f'Good Morning {name}')
    elif hour>12 and hour<=17:
        print(f'Good Afternoon {name}')
    else:
        print(f'Good Evening {name}')


# The function of the main game.
def generate_random_letter():
    print('''Choose the difficulty level 
    1.Easy
    2.Normal
    3.Hard
    4.Extreme''')
    user_input = int(input('Enter your choice here:- '))

    if user_input==1:
        word_lenth = 2
    elif user_input==2:
        word_lenth = 3
    elif user_input==3:
        word_lenth = 4
    elif user_input==4:
        word_lenth = 5
    Random_letters = RandomWord(max_word_size=word_lenth)
    letters = Random_letters.generate()


    # The instructions for the user.
    Instructions = f'''\nComputer has choosen {word_lenth} letters. 
Guess these {word_lenth} in 3 chances for each letter.\n'''
    print(Instructions)
    counter = 0        # This variable will count the number of chances of user to guess the letter.


    # This while statement will be keep running until the counter is less than 3.
    while counter<3:

        # This if statement will run when user_input will be equal to 1.
        if word_lenth==2:
            user_guess_1 = input('Guess both letters:- ')
            if user_guess_1==letters:
                print('The Letters are correct.\nWell Played!!')
            elif user_guess_1 !=letters:
                print("The letters are wrong.")
                counter = counter + 1
                
        # This elif statement will run when user_input will be equal to 2.
        elif word_lenth==3:
            user_guess_2 = input('Guess the 3 random letters:- ')
            if user_guess_2==letters:
                print('The letters are correct.\nWell Played!!')
            elif user_guess_2 !=letters:
                print('The letters are wrong.')
                counter = counter + 1
      
        # This elif statement will run when user_input will be equal to 3.
        elif word_lenth==4:
            user_guess_3 = input('Guess the 4 random letters:- ')
            if user_guess_3==letters:
                print('The letters are correct.\nWell Played!!')
            elif user_guess_3 !=letters:
                print('The letters are wrong.')
                counter = counter + 1
              
        # This elif statement will run when user_input will be equal to 4.
        elif word_lenth==5:
            user_guess_4 = input('Guess the 5 random letters:- ')
            if user_guess_4==letters:
                print('The letters are correct.\nWell PLayed!!')
            elif user_guess_4!= letters:
                print('The letters are wrong.')
                counter = counter + 1

    # This else statement will run when the counter will be equal to 3.
    else:
        print("\nYour all 3 chances are over.\nBetter Luck Next Time!!")  
        print(f'The correct letters are "{letters}"')          
                

try:
    greeting()
    generate_random_letter()

except Exception as e:
    print('Invalid input....')
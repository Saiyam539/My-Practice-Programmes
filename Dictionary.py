# This program will take input from the user
# and tell the meaning of that word with the 
# help of pydictionary module in python

import PyDictionary
import datetime

def greeting():
    print("*****\nWELCOME TO THE EVERY WORD DICTIONARY\n*****")
    name = input('Enter your name here:- ')

    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        print(f"Good Morning {name}")
    elif hour>12 and hour<=17:
        print(f'Good Afternoon {name}')
    else:
        print(f'Good Evening {name}')
    
def dictionary():
    from PyDictionary import PyDictionary
    dictionary = PyDictionary()

    Options = '''What would you like to do??
    1.Meaning of a word
    2.Synonym of a word
    3.Antonym of a word
    4.Exit'''
    print(Options)

    Options_input = int(input('Enter the option number here:- '))
    if Options_input==1:
        user_input = input("\nEnter the word here:- ")
        meaning_of_word = dictionary.meaning(user_input)
        print(f"The meaning of {user_input} is {meaning_of_word}.")

    elif Options_input==2:
        user_input = input("Enter the word here:- ")
        synonym_of_word = dictionary.synonym(user_input)
        print(f'The synonym of {user_input} is {synonym_of_word}.')
    
    elif Options_input==3:
        user_input = input('Enter the word here:- ')
        Antonym_of_word = dictionary.antonym(user_input)
        print(f'The antonym of {user_input} is {Antonym_of_word}.')
    elif Options_input==4:
        print('Thankyou for using Every Word Dictionary.')
        exit()
    else:
        print('Please enter a valid option.')

try:
    greeting()
    dictionary()
except Exception as e:
    print("An error occure..")
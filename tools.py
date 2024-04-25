'''
Link: https://github.com/StellaHerzberg/Project2-RPG.git 
Name: Stella Herzberg
Date: 04/18/2024
Class: CPSC 1050
Section: 001
Assignment: Project 2 RPG

Description: This file includes descriptions for all of the resources and tools used in the
gamy.py file. This file creates an RPG which leads through a cave and requires the user to 
complete a variety of obstacles to exit the cave.
'''
from game import game


class Item:
    '''Sets up a class for the Sword.'''

    def __init__(self, name, description, use):
        '''Initializes the name, description, and damage amount for the Sword.'''
        self.name = name
        self.description = description
        self.use = use
    
    def get_name(self):
        '''Returns the name of the object.'''
        return self.name

    def get_description(self):
        '''Returns the description of the game.'''
        return self.description

    def get_use(self):
        '''Returns the use of the tool.'''
        return self.use

    def tool_information(self):
        return f'{self.get_name}: {self.get_description}{self.get_use}'



def use_sword():
    '''Function to use the sword tool. Allows the user to defeat the beast automatically with no health depletion.'''
    pass
    

def use_potion(player):
    '''Function to use the potion. Grants the user + 50 health.'''

    # Gets current health from the player and increases it by 50
    current_health = player.get_health()
    new_health = current_health + 50

    print(f'\nYou take the potion. Your health increases by 50 and now stands at {health}')

    # Sets the player's health as the updated health
    player.set_health(new_health)


def use_resolver(question):
    correct_answer = question.get_correct()
    answer_choices = question.get_answer_choices()

    print('You will get two attempts to answer this question.')

    for i in range(2):
        print("Please enter your answer:")
        user_answer = input().strip().lower()

        answer_list = []
        for i in random_question.get_answer_choices():
            answer_list.append(str(i).lower())

        # Validates that user input is valid
            while user_answer not in answer_list:
                print(f'Invalid input. Please select one of the answer choices: {random_question.get_answer_choices()}')
                user_answer = input().lower().strip()
        
        if user_answer == correct_answer:
            print('Correct! You defeated the beast with no health damage!')
            return True 
        else:
            print(f'Incorrect answer.')
    
    return False
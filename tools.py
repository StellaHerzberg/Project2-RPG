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


class Item:
    '''Sets up a class for the Sword. Code for sword use is in game.py'''

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
    

def use_potion(player):
    '''Function to use the potion. Grants the user + 50 health.'''

    # Gets current health from the player and increases it by 50
    current_health = player.get_health()
    new_health = current_health + 50

    print(f'\nYou take the potion. Your health increases by 50 and now stands at {new_health}')

    # Returns the player's new health
    return new_health

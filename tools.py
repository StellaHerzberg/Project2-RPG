'''
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

'''
Name: Stella Herzberg
Date: 04/18/2024
Class: CPSC 1050
Section: 001
Assignment: Project 2 RPG

Description: This creates a RPG "Caveman" where the user interacts as a character within a cave. The user will attempt
to move through various rooms, each one containing either a treasure chest with supplies or a monster that they
must fight. The user wins if they successfully navigate through all of the rooms without dying.

This file creates the Rooms for the Adventure Map.
'''

class AdventureMap:
    '''Class created which includes all of the rooms in the adventure map.'''

    def __init__(self):
        '''Creates an empty dictionary for the rooms in the adventure map.'''
        self.map_dict = {}

    def add_room(self, room):
        self.map_dict[room.get_name().lower()] = room
    

class Room:
    '''Class created to access the attributes of an individual room.'''

    def __init__(self, name, description = ""):
        '''Initializes the name and description characteristics of the Room class.'''
        self.name = name
        self.description = description

    def get_name(self):
        '''Returns the name of the room.'''
        return self.name
    
    def get_description(self):
        '''Returns the description of the room.'''
        return self.description

    def __str__(self):
        '''Returns a string representation of the room's description and name.'''
        return f'{self.description} You are in the {self.name}.'
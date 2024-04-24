'''
Name: Stella Herzberg
Date: 04/18/2024
Class: CPSC 1050
Section: 001
Assignment: Project 2 RPG

Description: This creates a RPG "Caveman" where the user interacts as a character within a cave. The user will attempt
to move through various rooms, each one containing either a treasure chest with supplies or a monster that they
must fight. The user wins if they successfully navigate through all of the rooms without dying.
'''

# Imports various files to be used in the game
from questions import Questions
from tools import Item
from adventuremap import AdventureMap
from adventuremap import Room

import random


class InvalidInputError(Exception):
    '''Creates a class that takes the user's input for their desired room and creates an error message
    when called on.'''

    def __init__(self, message= "Invalid input. Try again."):
        '''Initialized the description of the error.'''
        self.error_message = message
    
    def __str__(self):
        '''Prints out the error message in a string format.'''
        return f'{self.error_message}'


class Character:
    '''Sets up a parent class for the characters in the game.'''

    def __init__(self, name, health = 200):
        '''Initalizes the name and health attributes for the Character class.'''
        self.name = name
        self.health = health


class Player(Character):
    '''Creates a class for the user's playing character.'''

    def __init__(self, name, health = 200):
        '''Initialies the name and health variables for the Player.'''
        super().__init__(name, health)

    def get_health(self):
        return self.health

    def health_increase(self, increase):
        '''Increases the Player health by a random amount.'''
        self.health += self.increase

    def health_decrease(self):
        '''Decreases the Player health by a random amount.'''
        decrease = randint(50,100)
        self.health -= decrease
        return self.health


class Monster(Character):
    '''Creates a class for the Monster that inherits from the Character class.'''

    def __init__(self, name, health):
        super().__init__(name, health)


def replay():
    '''When called, main function runs again.'''
    main()


def main():

    # Creates items for tools the user can receive (sword, potion, and resolver)
    sword = Item("Sword", "A shining blade, honed for battle, swift and lethal in skilled hands.", "User can eliminate an answer choice from the list of options.")
    potion = Item("Potion", "Vial of shimmering liquid, glowing with vitality, promising swift restoration to the wounded and weary.", "Adds 50 health to user.")
    resolver = Item("Resolver", "A beautiful stained glass offers the chance to correct mistakes and provide clarity.", "Grants the user an extra guess on a question with no health depletion.")

    # Creates an adventure_map object and adds the monster room and treasure room to the map
    adventure_map = AdventureMap()
    adventure_map.add_room(Room("The Beast's Lair", "Entering the room, a primal fear grips you as the air grows thick with tension. the faint glow of touchlight barely illuminates the massive silhouette lurking in the shadows - the unmistakable presence of a formidable beast."))
    adventure_map.add_room(Room("Treasure Trove", "Upon entering, you're enveloped in a comforting glow, surrounded by shelves adorned with an array of gleaming tools. At the heart of the room, a study workbench holds a versatile companion, eager to aid in your endeavors."))

    # Creates instances of the Question class for each individual question
    question1 = Question("Which country flied a green, white, and orange tricolor flag (in that order)?",["ireland", "france", "italy", "brazil"], "ireland")
    question2 = Question("Which of the following languages has the longest alphabet?", ["greek", "russian", "arabic", "english"], "russian")
    question3 = Question("What is the largest US state by landmass", ["texas", "california", "idaho", "alaska"], "alaska")
    question4 = Question("What is the strongest muscle in the human body?", ["jaw", "heart", "hamstring", "glute"], "jaw")
    question5 = Question("Which disney princess has blonde hair?", ["ariel", "cinderella", "snow shite", "belle"], "cinderella")
    question6 = Question("Who is known as 'The King of Pop'?", ["bruno mars", "beyonce", "nickelback", "michael jackson"], "michael jackson")
    question7 = Question("In atoms, which carries a positive charge?", ["protons", "neutrons", "electrons", "dna"], "protons")
    question8 = Question("What was the name of the Charlotte Hornets NBA team previously?", ["charlotte honeybees", "charlotte pelicans", "charlotte bobcats", "charlotte hawks"], "charlotte bobcats")
    question9 = Question("What year was the Declaration of Independence signed?", ["1608", "1818", "1742", "1776"], "1776")
    question10 = Question("In which Italian city was pizza first made?", ["naples", "rome", "florence", "milan"], "naples")


    # Welcome statements to explain the game to user
    print("Welcome to Caveman! You are currently stuck inside of a deep, dark cave. This cave is long and complex - you must move through \
    ten separate stages in order to leave. At each stage, you will have the choice of two rooms. Choose carefully! One room will contain a tool \
    to assist you in your travels while the other will contain a monster that you must beat in order to move forward.")
    print(f"\nTo win, you must navigate through all 10 stages without dying first. Your health will begin at 200. Good luck!")

    # Prompts user to input their name
    print(f"\nPlease enter your name to begin.")
    user_name = input()

    # Creates the user's player using their name
    player = Player(user_name)

    # Initiates tool_list and question_list
    tool_list = []
    question_list = [question1, quesition2, question3, question4, question5, question6, question7, question8, question9, question10]
    

### GAME LOOP
    # Loop continues while the player's health is above 0
    while player.get_health > 0:

        try:
        
            # Prompts user to choose a room
            print(f'\nPlease select which room to enter: 1 or 2')
            user_choice = input().strip()

            # Validates the user's input, raises the Error exception if input not valid
            while user_choice not in [1, 2]:
                raise InvalidInputError()

            # Gets a random integer from 0 to 1
            random_num = randint(0,1)

            # If the random number is 0, user enters monster room
            if random_num == 0:

                # Sets the room as the treasure room and prints it
                room = adventure_map.get_room("The Beast's Lair")
                print(room)

                print(f"\nTo defeat the monster, correctly answer the following question:")
                
                # Generates a random question from the question list
                random_question = random.choice(question_list)

                # Prints the question and its answer choices
                print(random_question.get_question)
                print(random_question.get_answer_choices)

                # Prompts user to input their answer
                print(f'\n{user_name}, what is your answer?')
                user_answer = input().lower().strip()
                
                # Creates a list for the answer choices in the question
                answer_list = []
                for i in random_question.get_answer_choices():
                    answer_list.append(str(i).lower())

                # Validates that user input is valid
                while user_answer not in answer_list:
                    raise InvalidInputError()
                    user_answer = input().lower().strip()

                # If user answers incorrectly, this is printed and the player's health decreases
                if user_answer != random_question.get_correct:
                    print(f"Oh no - that answer was incorrect! The beast lashes out and injures you, but luckily you are able to escape before he kills you! Your health now stands at {player.health_decrease}")

                # If user answers correctly, this is printed and user continues
                else:
                    print(f'Correct! You killed the beast before he was able to hurt you! You')

            # If the random number is 1, user enters the treasure room
            elif random_num == 1:
                
                # Sets room as the lair and prints it
                room = adventure_map.get_room("Treasure Trove")
                print(room)
                
                # Generates a random number between 0 and 2
                another_num = randint(0,2)

                # If the random number is 0, the user gets a sword
                if another_num == 0:
                    print(sword.tool_information)       # Prints sword info
                    tool_list.append("sword")           # Adds sword to tool list

                # If the random number is 1, the user gets a potion
                elif another_num == 1:
                    print(potion.tool_information)      # Prints information
                    tool_list.append("potion")          # Adds potion to sword list

                # If the random number is 2, the user gets the resolver
                elif another_num == 2:
                    print(resolver.tool_information)        # Prints resolver information
                    tool_list.append("resolver")            # Adds resolver to list
            

            # Except block catches exception and prints it
            except InvalidInputError as e:
                print(e)



if __name__ == "__main__":
    main()
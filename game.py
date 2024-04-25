'''
Link: https://github.com/StellaHerzberg/Project2-RPG.git 
Name: Stella Herzberg
Date: 04/18/2024
Class: CPSC 1050
Section: 001
Assignment: Project 2 RPG

Description: This creates a RPG "Caveman" where the user interacts as a character within a cave. The user will attempt
to move through various rooms, each one containing either a treasure chest with supplies (a sword, potion, or a resolver) or a monster that they
must fight. The user wins if they successfully navigate through all of the 10 rooms without dying.
'''

# Imports various files to be used in the game
from questions import Questions
from tools import (Item, use_sword, use_potion, use_resolver)
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
        return int(self.health)

    def set_health(self, health):
        self.health = health

    def health_increase(self, increase):
        '''Increases the Player health by a random amount.'''
        self.health += self.increase

    def health_decrease(self):
        '''Decreases the Player health by a random amount.'''
        decrease = random.randint(50,100)
        self.health -= decrease
        return self.health


class Monster(Character):
    '''Creates a class for the Monster that inherits from the Character class.'''

    def __init__(self, name, health):
        super().__init__(name, health)


def monster_room(question_list, player):
    '''Executes the monster room. Takes the question, answer choices, and the correct answer and prompts the user to answer it. If the response is correct,
    the function will return True. If the response is incorrect, the function will return False.'''

    # Generates a random question from the question list
    random_question = random.choice(question_list)

    # Prints the question and its answer choices
    print(random_question.get_question())
    print(random_question.get_answer_choices())

    # Prompts user to input their answer
    print(f'\nWhat is your answer?')
    user_answer = input().lower().strip()
                
    # Creates a list for the answer choices in the question
    answer_list = []
    for i in random_question.get_answer_choices():
        answer_list.append(str(i).lower())

    # Validates that user input is valid
    while user_answer not in answer_list:
        print(f'Invalid input. Please select one of the answer choices: {random_question.get_answer_choices()}')
        user_answer = input().lower().strip()

    # If user answers incorrectly, this is printed and the player's health decreases
    if user_answer != random_question.get_correct():
        return True

    # If user answers correctly, this is printed and user continues
    else:
        print(f'Correct! You killed the beast before he was able to hurt you! You continue on to the next room with {player.get_health()} health.')
        question_list.remove(random_question)
        return False
        


def replay():
    '''When called, game will replay and main function runs again.'''
    main()



def main():

    # Creates items for tools the user can receive (sword, potion, and resolver) - includes the name, description, and its use
    sword = Item("sword", "A shining blade, honed for battle, swift and lethal in skilled hands.", "This tool effectively kills the beast with no health depletion to the user.")
    potion = Item("potion", "Vial of shimmering liquid, glowing with vitality, promising swift restoration to the wounded and weary.", "Adds 50 health to user.")
    resolver = Item("resolver", "A beautiful stained glass offers the chance to correct mistakes and provide clarity.", "Grants the user an extra guess on a question with no health depletion.")

    # Creates an adventure_map object and adds the monster room and treasure room to the map - includes the name and description
    adventure_map = AdventureMap()
    adventure_map.add_room(Room("The Beast's Lair", "Entering the room, a primal fear grips you as the air grows thick with tension. the faint glow of touchlight barely illuminates the massive silhouette lurking in the shadows - the unmistakable presence of a formidable beast."))
    adventure_map.add_room(Room("Treasure Trove", "Upon entering, you're enveloped in a comforting glow, surrounded by shelves adorned with an array of gleaming tools. At the heart of the room, a study workbench holds a versatile companion, eager to aid in your endeavors."))

    # Creates instances of the Question class for each individual question: includes question, answer choices, and the correct answer
    question1 = Questions("Which country flied a green, white, and orange tricolor flag (in that order)?",["france", "italy", "brazil", "ireland"], "ireland")
    question2 = Questions("Which of the following languages has the longest alphabet?", ["greek", "russian", "arabic", "english"], "russian")
    question3 = Questions("What is the largest US state by landmass", ["texas", "california", "idaho", "alaska"], "alaska")
    question4 = Questions("What is the strongest muscle in the human body?", ["heart", "jaw", "hamstring", "glute"], "jaw")
    question5 = Questions("Which disney princess has blonde hair?", ["ariel", "cinderella", "snow white", "belle"], "cinderella")
    question6 = Questions("Who is known as 'The King of Pop'?", ["bruno mars", "beyonce", "nickelback", "michael jackson"], "michael jackson")
    question7 = Questions("In atoms, which carries a positive charge?", ["neutrons", "electrons", "protons", "dna"], "protons")
    question8 = Questions("What was the name of the Charlotte Hornets NBA team previously?", ["charlotte honeybees", "charlotte pelicans", "charlotte bobcats", "charlotte hawks"], "charlotte bobcats")
    question9 = Questions("What year was the Declaration of Independence signed?", ["1608", "1818", "1742", "1776"], "1776")
    question10 = Questions("In which Italian city was pizza first made?", ["rome", "florence", "naples", "milan"], "naples")


    # Welcome statements to explain the game to user
    print(f"\nWelcome to Caveman! You are currently stuck inside of a deep, dark cave. This cave is long and complex - you must move through ten separate stages in order to leave. At each stage, you will have the choice of two rooms. Choose carefully! One room will contain a tool to assist you in your travels while the other will contain a monster that you must beat in order to move forward.")
    print(f"\nTo win, you must navigate through all 10 stages without dying first. Your health will begin at 200. Good luck!")

    # Prompts user to input their name
    print(f"\nPlease enter your name to begin.")
    user_name = input()

    # Creates the user's player using their name
    player = Player(user_name)

    # Initiates tool_list, question_list, a count for the rooms, the player's tool list, and a user_tool_choice variable
    tool_list = [sword, potion, resolver]
    question_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
    count = 0
    player_tool_list = []
    user_tool_choice = "no"
    

### GAME LOOP
    # Loop continues while the player's health is above 0
    while player.get_health() > 0 and count <= 10:

        try:
        
            # Prompts user to choose a room
            print(f'\nPlease select which room to enter: 1 or 2. You have successfully completed {count} rooms.')
            user_choice = input().strip()

            # Validates the user's input, raises the Error exception if input not valid
            while user_choice not in ["1", "2"]:
                raise InvalidInputError()

            # Gets a random integer from 0 to 1
            random_num = random.randint(0,4)


            # MONSTER ROOM: executes if the random_num is 0 through 3
            if random_num in [0, 1, 2, 3]:

                # Sets the room as the treasure room and prints the introductive room lines
                room = adventure_map.get_room("The Beast's Lair")
                print(room)
                print(f"To defeat the monster, correctly answer the following question:\n")
            

                # If the user does not have any tools, this is printed and this code is executed
                if len(player_tool_list) == 0:
                    print(f'You will not be using a tool to aid your fight.')
                    
                    # If monster_room returns True, the user answered incorrectly. Their health is depleted.
                    if monster_room(question_list,player): 
                        print(f"Oh no - that answer was incorrect! The beast lashes out and injures you. Your health now stands at {player.health_decrease()}.")
                        count += 1
                    else:
                        count += 1
                        
                        
                # Executes if the player currently has tools. Asks if user wants to use a tool then takes it in as user_tool_choice
                if len(player_tool_list) > 0:
                    print(f'\nYou have tools avaliable. Do you want to use a tool? Y or N')
                    user_tool_choice = input().lower().strip()
                    
                    # If the user wants to use a tool
                    if user_tool_choice == "y":

                        # Prints out the name and description of the player's tools
                        print('Your tools:')
                        for item in player_tool_list:
                            print(f'{item.get_name()}: {item.get_description()}')

                        # Prompts player to choose the tool they want to use - prints the list of tools and takes their choice as user_tool_choice
                        print(f'\nPlease select which tool you would like to use.')
                        print([tool.get_name().lower() for tool in player_tool_list])
                        user_tool_choice = input().lower().strip()
                        
                        # Validates that the user's input is one of their tools, if not an error is printed and another input is taken
                        while user_tool_choice not in [tool.get_name().lower() for tool in player_tool_list]:
                            print(f'Please input a valid tool name.')
                            user_tool_choice = input().lower().strip()

                        print(f'You selected the {user_tool_choice}')           # Prints the user's tool choice

                        # Executes if the user chose the sword tool
                        if user_tool_choice == "sword":
                            
                            # Executes the function with the sword's use
                            print('You successfully killed the monster with no health depletion!')
                            
                            # Iterates the count variable by 1
                            count += 1 

                            # Removes the sword from the player_tool_list by iterating through the list, getting the name of the object, and removing it
                            for tool in player_tool_list:
                                if tool.get_name().lower() == "sword":
                                    player_tool_list.remove(tool)
                                    break
                
                        # Executes if the user chooses to use the resolver
                        elif user_tool_choice == "resolver":
                                
                            # Generates a random question from the question list
                            random_question = random.choice(question_list)
                            
                            # Executes the function with the resolver's use
                            use_resolver(random_question)

                            # Iterates count variable
                            count += 1
                            
                            # Removes the resolver from the player's tool list by iterating through the list, getting the name of the object, and removing it
                            for tool in player_tool_list:
                                if tool.get_name().lower() == "resolver":
                                    player_tool_list.remove(tool)


                    # If the user does not want to use a tool, loop is broken and count is iterated by 1
                    else:
                        if monster_room(question_list,player): 
                            print(f"Oh no - that answer was incorrect! The beast lashes out and injures you. Your health now stands at {player.health_decrease()}.")
                            count += 1
                            break


            # If the random number is 4, user enters the treasure room
            elif random_num == 4:
                
                # Sets room as the lair and prints it
                room = adventure_map.get_room("Treasure Trove")
                print(room)

                # Generates a random tool and prints the name, description, and use
                random_tool = random.choice(tool_list)
                print(f'\nYou found a {random_tool.get_name()}: {random_tool.get_description()}\n Use: {random_tool.get_use()}')

                # Adds the random tool to the player's list
                player_tool_list.append(random_tool)
                
                # If the random tool is the potion, this executes
                if random_tool.get_name().lower() == "potion":
            
                    # Iterates through the player's tool list, gets the name of the potion, executes the use_potion functionm then removes it
                    for tool in player_tool_list:
                        if tool.get_name().lower() == "potion":
                            player.set_health = use_potion(player.get_health())
                            player_tool_list.remove(tool)

                # Prompts user to acknowledge the tool
                print(f'Press any key to accept your treasure and continue.')
                user_choice = input()

                # Iterates count by 1
                count += 1


        # Except block catches exception and prints it
        except InvalidInputError as e:
            print(e)


### END GAME
    # If the player's health is less than 0 or if player has been through 10 rooms
    if count < 10 and player.get_health() <= 0:

        # This prints and a user input is taken
        print(f'GAME OVER. You died before you could escape the cave. Better luck next time.')
        print(f'Would you like to play again? Y or N')
        user_choice = input().strip().upper()
        final = "lost"

        # Validates the user's input 
        while user_choice not in ["Y", "N"]:
            print(f'Invalid input. Please select either Y or N')
            user_choice = input().strip().upper()

    # If the count is 10 and player's health is above 0
    elif count == 10 and player.get_health() > 0:

        # This is printed, asks user if they want to play again, then takes response as input
        print(f'Congratulations, {user_name}! You successfully escaped the cave! Would you like to play again? Y or N')
        user_choice = input().strip().upper()
        final = "won"

        # Validates the user's input
        while user_choice not in ["Y", "N"]:
            print(f'Invalid input. Please select either Y or N')
            user_choice = input().strip().upper()
    

    # If the user chooses to restart the game, this prints, and replay() function executes
    if user_choice == "Y":
        print(f'Restarting game...')
        replay()
    
    # If user does not want to restart
    elif user_choice == "N":

        # Opens the output.txt file, writes a line, then closes it
        with open('output.txt', 'w') as output:
            output.write(f"You {final}! You completed {count} rooms.")
        output.close()


if __name__ == "__main__":
    main()
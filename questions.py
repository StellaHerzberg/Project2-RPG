'''
Link: https://github.com/StellaHerzberg/Project2-RPG.git 
Name: Stella Herzberg
Date: 04/18/2024
Class: CPSC 1050
Section: 001
Assignment: Project 2 RPG

Description: This creates a RPG where the user interacts as a character within a cave. The user will attempt
to move through various rooms, each one containing either a treasure chest with supplies or a monster that they
must fight. The user wins if they successfully navigate through all of the rooms without dying.

This file includes all of the questions that may be asked when the user is "fighting the monster".
'''

class Questions:
    '''Class contains 10 questions for the user to answer if they choose a monster room.'''

    def __init__(self, question, answer_choices, correct):
        '''Initiates a question and all of its characteristics.'''
        self.question = question
        self.answer_choices = answer_choices
        self.correct = correct

    def get_question(self):
        '''Returns the question itself.'''
        return self.question

    def get_answer_choices(self):
        '''Returns the list of answer choices for of the question.'''
        return self.answer_choices

    def get_correct(self):
        '''Returns the correct answer of the question.'''
        return self.correct
      
      
''' 
question1 = Question("Which country flied a green, white, and orange tricolor flag (in that order)?",["Ireland", "France", "Italy", "Brazil"], "ireland")
question2 = Question("Which of the following languages has the longest alphabet?", ["Greek", "Russian", "Arabic", "English"], "russian")
question3 = Question("What is the largest US state by landmass", ["Texas", "California", "South Carolina", "Alaska"], "alaska")
question4 = Question("What is the strongest muscle in the human body?", ["Jaw", "Heart", "Hamstring", "Glute"], "jaw")
question5 = Question("Which disney princess has blonde hair?", ["Ariel", "Cinderella", "Snow White", "Belle"], "cinderella")
question6 = Question("Who is known as 'The King of Pop'?", ["Bruno Mars", "AC/DC", "Hootie & the Blowfish", "Michael Jackson"], "michael jackson")
question7 = Question("In atoms, which carries a positive charge?", ["Protons", "Neutrons", "Electrons", "DNA"], "protons")
question8 = Question("What was the name of the Charlotte Hornets NBA team previously?", ["Charlotte Honeybees", "Charlotte Pelicans", "Charlotte Bobcats", "Charlotte Hawks"], "charlotte bobcats")
question9 = Question("What year was the Declaration of Independence signed?", ["1608", "1818", "1742", "1776"], "1776")
question10 = Question("In which Italian city was pizza first made?", ["Naples", "Rome", "Florence", "Milan"], "naples")
'''
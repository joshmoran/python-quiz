import json 
import os 
import glob

data = {
    "name": "UK Capitals",
    "description": "Here be monsters",
    "questions": {
        "City of the uk": {
            "A": "Option 1",
            "B": "Option 2",
            "C": "Option 3",
            "D": "Option 4",
            "S": "Skip",
            "answer": "B"
        },
        "City of luxemburg": {
            "A": "Option 1",
            "B": "Option 2",
            "C": "Option 3",
            "D": "Option 4",
            "S": "Skip",
            "answer": "B"
        },
        "City of france": {
            "A": "Option 1",
            "B": "Option 2",
            "C": "Option 3",
            "D": "Option 4",
            "S": "Skip",
            "answer": "B"
        }
    }
}



def create_quiz ( data ):
  # Function Variables
  total_questions = len( data )
  current_question = 0
  correct_answers = 0

  for key, value in data.items():
      if key != 'name' and key != 'description':
          print(f"Okay, lets start!")
          for question, answers in value.items():
            print("---------------------------")
            print("")           
            print(f"Question {current_question + 1}: {question}")
            print("")
            incorrect = []    
            for selector, meaning in answers.items():
              if selector == 'answer':
                correct = meaning
                while ( correct in incorrect):
                  incorrect.remove( correct)
              else:
                if selector == 'S':
                  incorrect.append(selector)
                  print("")
                  print(f"{selector} - no potential points can be gained")
                  print("")
                else:
                  incorrect.append( selector )
                  print(f"{selector}: {meaning}")
            user_answer = input('Which answer is correct? ')
            print("")
            while user_answer not in incorrect and user_answer != correct:
              user_answer = input('Which answer is correct? ')
            if user_answer != correct:
              print("")
              print(f"Sorry, that's incorrect. The correct answer is {correct}")
              print("")
            else:        
              correct_answers += 1
              print("")
              print(f"Thats correct!! your total points are now {correct_answers}")
              print("")

              
            current_question += 1
          #   if option != 'answer':
          #     print(f"{option}. {meaning}")
          #   

print(f"You got {correct_answers} out of {total_questions}")

# user_name = input("What is your name? ")
# print()

# # Initial Variables
# total_questions = 5
# correct_answers = 0

# print('Welcome to the Python Quiz!')
# print('This quiz will have 5 questions. You will be given 4 options for each question.')
# print()


# # 
# # Question 1 - How do you define a function in Python?
# # 
# print('How would you define a function in Python?')
# print('A: def functionName:')
# print('B: func functionName')
# print('C: fc functionName')
# print('D: function functionName')
# print('S: Skip Question')

# try {

# }
# answer1 = input('Please pick one of the answers')

#
# Question 2
# 


# 
# Question 3 
# 


# 
# Question 4 
# 


# 
# Question 5 
# 




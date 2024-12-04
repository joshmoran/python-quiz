# Import Modules
import glob
import json

# User Variables 
quiz_dir = 'quizzes/'
taken_quizzes = []
available_quizzes = []

# System Variables
selected_pathname = ''
selected_name = '' 
selected_json = {}
user_name = ''

quiz_files = glob.glob( quiz_dir + '*.json')

# Initial Initialization 
def initialise():
  global user_name
  checking = False
  print("Hello and welcome to quizzes")
  print("")
  print('To begin, please enter your name:')
  while not checking and len(user_name) > 0:
    user_name = query_user()
    checking = True
  print("") 
  print(f"Hello and welcome {user_name}")
  print("")
  print("Lets test your knowledge with our quizzes!!!")
  print("")
  load()

def query_user():
  try:
    new_user_name = input('>>> ' )
    if new_user_name:
      raise ValueError
    else:
      raise Exception
    print()
    print()
  except Exception:
    try:
      query_user_detailed_exceptions( new_user_name, 'string' )
    except:
      query_user_detailed_exceptions( new_user_name, type(int()) )
    print('Invalid input. Please enter your name.')
    return query_user()
  return True

def query_user_detailed_exceptions( checking_user_name, data_type = 'int' ):
  repeated = False
  checking_user_name = int(checking_user_name)
  while not repeated:

    print()
    if int(checking_user_name) >= 0 or int(checking_user_name) <= 0:
      print('Please not a number. Please enter your name.')
    elif data_type =='string':
      if len(checking_user_name) == 0:
        print("Not an empty string. Please enter your name")
      else:
        print('Please not a string. Please enter your name.')
    elif data_type == 'list':
      print('Please not a list. Please enter your name.')
    new_user_name = input('>>> ' )
    if len(new_user_name) < 1 or new_user_name == '':
      repeated = False
  print('Invalid input. Please enter your name.')
  return True
# Basic Menu
def load():
  global available_quizzes

  indexQuiz = 1

  # If previous quizzes taken, show results
  if len(taken_quizzes) > 0:
    print("")
    print('Previous Results')
    print("")
    for result in taken_quizzes:
      print(f"    {result[0]} -----  {result[1]}%")
    print("")
  # List JSON Quizzes 
  print( 'Selector --- Name')
  print("")
  for quiz_file in quiz_files:
    filepath = quiz_file

    with open(filepath, 'r') as file:
      data = json.load(file)

    for key, value in data.items():
      if key == 'name':
        print(f'    {indexQuiz} -----  {value}')
        new_quiz = [ indexQuiz, filepath ]
        available_quizzes.append( new_quiz )
    indexQuiz += 1
  select_quiz()
  
# User input to select a quiz 
def select_quiz ( ):
  global available_quizzes
  correct_input = True
  print("")
  while correct_input:
    print("Please select a number to start a quiz:")
    selected_quiz = input('>>> ')
    try:
      chosen = int(selected_quiz)
      if chosen not in range( 0, len(available_quizzes) ):
        print('Invalid input. Please enter a number between 1 and', len(available_quizzes))
        continue
      else:
        set_quiz( chosen )
      correct_input = False
    except ValueError:
      print('Invalid input. Please enter a number between 1 and', len(available_quizzes)) 

# Set quiz from users input 
def set_quiz ( selector ):
  for quiz in available_quizzes:
    if quiz[0] == selector:
      selected_pathname = quiz[1]

      with open(selected_pathname, 'r') as file:
        selected_json = json.load(file)
      for key, value in selected_json.items():
        if key == 'name':
          selected_name = value
          print("")
          print(f"Okay you have selected {value}")
          print("")
  create_quiz( selected_json, selected_name )
    
# Create quiz from JSON file
def create_quiz ( data, name ):
  # Function Variables
  global user_name
  total_questions = len( data )
  correct_answers = 0

  for key, value in data.items():
    if key != 'name' and key != 'description':
      current_question = 1
      total_questions = len(value)
      print(f"Okay, lets start!")
      print("")
      for question, answers in value.items():
        print("---------------------------")
        print("")           
        print(f"Question {current_question}: {question}")
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
        user_answer = input('Which answer is correct? ').upper()
        print("")
        while user_answer not in incorrect and user_answer != correct:
          print("")
          print('Which answer is correct? ')
          user_answer = input(">>>").upper()
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
  print("")
  load_score( correct_answers, total_questions, name )

import math

def load_score( user_score, total_score, quiz_name ):
  # How to view scores
  # 100 to 90 - Grade A
  # 89 to 80 - Grade B
  # 79 to 70 - Grade C
  # 69 to 60 - Grade D
  # 59 to 50 - Grade E
  # 49 to 0 - Grade F
  global user_name

  if user_score == 0:
    percentage = 0
  else:
    percentage = ( total_score / user_score) * 100

  message = ''

  if user_score >= ( total_score * 0.9 ) and user_score <= total_score:
      print(f"Well done {user_name}, you got {user_score} out of {total_score} correct, thats", roundNumber( percentage ), "% scored correctly. Well done!!!")
  elif user_score >= ( total_score * 0.8 ) and user_score <= ( total_score * 0.89 ):
      print(f"Not bad {user_name} you got {user_score} out of {total_score} correct, thats", roundNumber( percentage ), "% scored correctly.  You can do better.")
  elif user_score >= ( total_score * 0.7 ) and user_score <= ( total_score * 0.79 ):
      print(f"Keep trying {user_name} you got {user_score} out of {total_score} correct, thats", roundNumber( percentage ), "% scored correctly.  You can improve.")
  elif user_score >= ( total_score * 0.6 ) and user_score <= ( total_score * 0.69 ):
      print(f"Not good {user_name} you got {user_score} out of {total_score} correct, thats", roundNumber( percentage ), "% scored correctly.  Better luck next time.")
  else: 
      print(f"You failed {user_name} you got {user_score} out of {total_score} correct, thats", roundNumber( percentage ), "% scored correctly.  Better luck next time.")
  create_result = [ quiz_name, percentage ]
  taken_quizzes.append( create_result )
  print("")
  print("Returning to the main menu")
  print("")
  load() 

def roundNumber ( score ):
   return round(score)
# Run on load
initialise()





# Quiz App
## This is an assignment for 'JustIT' within their technical training for Python
- Please see 'Project Brief.pdf' for full project details that this script must meet 
- Overview
[X] 1. Welcome message 
[X] 2. Display questions 
[X] 3. User input
[X] 4. Calculate score 
[X] 5. Display results
[X] 6. Data validation 
[X] 7. Thank you message

## Index
1. Overview and Error Handling
2. Adding new quizzes

# 1. Overview and Features

## Initial Start 
### Overview 
- Greets the user and welcomes them to the game 
- Asks user for their name 

### Error Handling 
- Users input for their name is error handled
- If a number is entered, an error is returned and the user is re-asked their name 
- If an empty string is entered, an error is returned and the user is re-asked their name 

## Rules
### Overview
- Show the user how to play the game
- Breaks down into two sections
    1. Selecting a quiz
    2. Answering questions 
- Asks user to enter a random key before continuing to the main menu 
   
## Main Menu
### Overview
- Shows the user two things:
  1. If previous quizzes have been taken, the quiz name and percentage score is shown
  2. Reads the 'quizzes/' directory and lists quizzes based on the JSON files
    - Get the name of the quiz and adds an index value

## Selecting a quiz 
### Error Handling
- Select quiz is error handled
- Making sure the user can only select an index that is present and valid 
  - E.g. their are 3 quizzes available and the user enters '4', this would return an error and re-asks the user to re-enter their selector 

## Create Quiz
### Overview 
- The quiz name is shown 
- The quiz description is how 
- Questions are read from the JSON file and are returned one-by-one once the user has selected a valid input (A,B,C,D or S)
  - Within the JSON, each question will have a key called 'answer' which indicates to the Python script which question option is correct.
    - THE QUESTION OPTION SELECTORS NEEDS TO BE A CAPITAL!!!
- At the end of the quiz
  - The users score is shown and a dynamic message is shown based on their score
  - The users score is saved into an array and can be shown when they are in the main menu (selecting a quiz)

### Error Handling 
- If the user does not enter a valid input, the user is re-asked to enter a valid input
- Until a valid input is entered, the question will not move on to the next questionUpdates to README

# 2. Adding new quizzes
- File in the root directory called, 'template.json'
- Edit this file
  - Change name
  - Change description
  - Add questions
  - Change question options 
    - Keep 'S' as is, this is used to skip the question
    - Change answer to the uppercase selector (A, B, C or D)
- Add file to the 'quizzes/' directory 
- Run the script and the main menu will have scanned the 'quizzes/' directory and added it to the main menu
- Scoring is done dynamically, so not matter on how many questions you add, the score output will be dynamic and based around a percentage 
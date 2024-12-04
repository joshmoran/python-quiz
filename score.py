import math

def load_score( user_score, total_score, user_name ):
    # How to view scores
    # 100 to 90 - Grade A
    # 89 to 80 - Grade B
    # 79 to 70 - Grade C
    # 69 to 60 - Grade D
    # 59 to 50 - Grade E
    # 49 to 0 - Grade F

    percentage = (user_score / total_score) * 100

    message = ''

    if user_score >= ( total_score * 0.9 ) and user_score <= total_score:
        print(f"Well done {user_name}, you got {user_score} out of 5 correct, thats", roundNumber( percentage ), "% scored correctly. Well done!!!")
    elif user_score >= ( total_score * 0.8 ) and user_score <= ( total_score * 0.89 ):
        print(f"Not bad {user_name} you got {user_score} out of 5 correct, thats", roundNumber( percentage ), "% scored correctly.  You can do better.")
    elif user_score >= ( total_score * 0.7 ) and user_score <= ( total_score * 0.79 ):
        print(f"Keep trying {user_name} you got {user_score} out of 5 correct, thats", roundNumber( percentage ), "% scored correctly.  You can improve.")
    elif user_score >= ( total_score * 0.6 ) and user_score <= ( total_score * 0.69 ):
        print(f"Not good {user_name} you got {user_score} out of 5 correct, thats", roundNumber( percentage ), "% scored correctly.  Better luck next time.")
    else: 
        print(f"You failed {user_name} you got {user_score} out of 5 correct, thats", roundNumber( percentage ), "% scored correctly.  Better luck next time.")

def roundNumber ( score ):
   return round(score)
load_score( 5, 5, 'Josh')
acceptable_username = False
username = ''
while not acceptable_username and not username:
    try:
        print("What is your username ")
        user_name = input(">>> ")

        try:
            if isinstance( int(user_name), int):
                print("")
                raise ValueError
                exit
        except ValueError:
            num_user_name = None
            exit

        if not user_name:
            print("")
            print("This is an empty string. please re-enter your name again")
            exit
        elif isinstance( user_name, str): 
            
            if len( user_name) > 1:
                try: 
                    # print( isNaN(user_name))
                    if user_name:
                        acceptable_username = True
                        username = user_name
                        print("Yes, this is your username", user_name)
                    elif int(user_name) <=0 or int(user_name) >= 0:
                        print("")
                        print("Please do not enter an integer")
                        raise ValueError
                        
                except ValueError:
                    print(username)
                    if username != '':
                        acceptable_username = True

                    print("Yes an errro")
                    exit
                
            elif isinstance( int(user_name), int ):                
                print("")
                print("This is a number, please re-enter your name again")
                exit

            # if num_user_name:
            #     print("This is a number")
            # else:
            #     print("Yes, this is your username", user_name)
        # else:
        #     if isinstance( num_user_name, int ):
        #         print("This is a number")
        #     else:
        #         if len( user_name) > 0:
        #             print("Yes, this is your username", user_name)
        #         else:
        #             print("This is an empty string")
    
    except Exception:
        if username != '':
            print("There has been an error, please try again")
        else:
            acceptable_username = True

print(f"The username is {user_name}")
#     >>>isinstance(1,str)
# False
# >>>isinstance('stuff',str)
# True
# >>>isinstance(1,int)
# True
# >>>isinstance('stuff',int)
# False
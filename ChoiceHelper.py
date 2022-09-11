import random;

# this script will randomly gen a yes or no, and also a random number
# have the user selected if they want a number or a yes no

print("""Cannot make a choice well let me help
        [1] will get you a random number between 1-100
        [2] will get you a random YES or No
        [3] Exit program
""")
user_input = 0
# keep looping so user can try multiple times
while user_input != "3":
    # get user input
    user_input = input("Enter your choice: ")
    # test input 
    if user_input == "1":
        #get ran int 
        the_number_is = random.randint(1,100)
        print(the_number_is)
    elif user_input == "2":    
        ran_bool = random.choice([True,False])
        # convert bool, to yes or no
        if ran_bool:
            print("YES")
        else:
            print("NO")
            #check if user is finished
    elif user_input == "3":
        quit()
        #catch all
    else:
        print("""Your input was incorrect, please try again
                [1] will get you a random number between 1-100
                [2] will get you a random YES or No
                [3] Exit program
        """)




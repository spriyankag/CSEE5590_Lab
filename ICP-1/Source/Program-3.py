import random
#using random interger function
random_number = random.randint(0,9)

#conditional statements
for i in range(0,9):
    # Initializing varible and assigning it to user input
    # convert string to int
    user_guess = int(input("Enter a number between 1 to 9:"))
    if(random_number > user_guess):
        print("Your answer is low than required")
    elif(random_number < user_guess):
        print("Your answer is high than required")
    else:
        print("Your Answer is PERFECT!!Congratulations!!")
        break





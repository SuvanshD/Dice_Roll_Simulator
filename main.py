import random

min_val = 1
max_val = 6

roll_again = "Yes"

while roll_again == "Yes" or roll_again == "Y":
    
    print("Rolling the dice ...")
    print("Values are : ")
    
    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))
    
    roll_again = input("Roll the Dices again :").capitalize()
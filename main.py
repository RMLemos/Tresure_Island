
print("Welcome to Tresure Island.\nYour mission is to find the tresure.")
start_point = input("You're at a cross road.\nWhere do you want to go? Type 'left' or 'right'\n").lower()

if start_point == 'right':
    print("You fell into a hole. Game over.")
elif start_point == 'left':
    print("You come to a lake. There is an island in the middle of the lake.")
    second_point = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    
    if second_point == 'swim':
        print("You got attacked by an angry trout. Game over.")
    elif second_point == 'wait':
        print("you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        final_point = input("Wich colour do you choose? Type 'red', 'yellow' or 'blue'.\n").lower()
        if final_point == 'red':
            print("It's a room full of fire. Game over.")
        elif final_point == 'blue':
            print("It's a room full of beasts. Game over.")
        elif final_point == 'yellow':
            print("You found the tresure! You win.")
        else: 
            print("you chose a door that doesn't exist. Game Over.")
    else: 
        print("you did not enter a valid character.")
else: 
    print("you did not enter a valid character.")
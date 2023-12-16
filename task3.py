import random

# This function is used for the Sncak 

def Snack(pn):
    
    if(pn == 17): 
        return 10
    elif(pn == 63):
        return 44
    elif(pn == 87):
        return 51
    elif(pn == 93):
        return 20
    elif(pn == 95):
        return 30
    elif(pn == 98):
        return 19
    else:
        return 0
        
# This function used for the Ladder 

def Ladder(pn):
    
    if(pn == 2): 
        return 36
    elif(pn == 4):
        return 10
    elif(pn == 21):
        return 21
    elif(pn == 28):
        return 56
    elif(pn == 53):
        return 14
    elif(pn == 72):
        return 19
    else:
        return 0


# Here we are create Snack Ladder Game 

player_1 = 1
player_2 = 1

player1Name = input("Enter Your Name(Player-1) : ")
player2Name = input("Enter Your Name(Player-2) : ")
print("\n")

while(player_1 <= 100 and player_2 <= 100):
    
    # Here first term is a player-1
    print(f"--> {player1Name}'s term <--")
    num1 = (int)(input("Enter the number 1 for Throw Dice & 0 for Aboard Game : "))
    if(num1 == 1):
        randnum1 = ((random.randrange(9))) % 6 +1  # random.randrange(9)  genrate the number between 1 to 9
        print(f"Player-1 dice number is {randnum1}")
        player_1 = player_1 + randnum1
        val1f=player_1
        print(f"Now palyer-1 position is {player_1}")
        player_1 = player_1 - Snack(player_1)
        if(player_1 != val1f):
            print(f"🔴 After Snack Efect position is {player_1}")
        val1h = player_1
        player_1 = player_1 + Ladder(player_1)
        if(player_1 != val1h):
            print(f"🟢 After Ladder Efect position is  {player_1}")
    elif(num1 == 0):
        break
    else:
        print("Pls Enter right number !")
        
    # Here first term is a player-2
    print(f"\n--> {player2Name}'s term <--")
    num2 = (int)(input("Enter the number 1 for Throw Dice & 0 for Aboard Game : "))
    if(num2 == 1):
        randnum2 = ((random.randrange(9))) % 6 +1
        print(f"Player-2 dice number is {randnum2}" )
        player_2 = player_2 + randnum2
        val2f =player_2
        print(f"Now palyer-2 position is {player_2}")
        player_2 = player_2 - Snack(player_2)
        if(player_2 != val2f):
            print(f"🔴 After Snack Efect position is {player_2}")
        val2h=player_2
        player_2 = player_2 + Ladder(player_2)
        if(player_2 != val2h):
            print(f"🟢 After Ladder Efect position is  {player_1}")
    elif(num2 == 0):
        break
    else:
        print("Pls Enter right number !")
        
    # Here we are check the who is win the game 
    if(player_1 >= 100):
        print("\nPlayer-1 Won the Game")
    elif(player_2 >= 100):
        print("\nPlayer-2 Won the Game")
        
    print("\n.........................................................................\n")
    
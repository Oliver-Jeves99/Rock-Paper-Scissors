import random

valid_moves = ["rock", "paper", "scissors", ""]
winner = "test"
play_game_flag = True 

while play_game_flag and winner != "You Win!":
    while True:
        player_move = input("Rock, Paper, Scissors....  ").lower()
        if player_move in valid_moves:
            break
        else:
            print("Invalid move! Please choose Rock, Paper, or Scissors.")
           
           
    Ai_move = random.randint(1,3)
    
    if Ai_move == 1:
        Ai_move = "Rock"
    elif Ai_move == 2:
        Ai_move = "Paper"
    elif Ai_move == 3:
        Ai_move = "Scissors"
    else:
        print("error!!")
       
    
    print(f"The Other player went for {Ai_move}")
    
    if player_move.lower() == "rock" and Ai_move.lower() == "scissors":
        winner = "You Win!"
    elif player_move.lower() == "paper" and Ai_move.lower() == "rock":
        winner = "You Win!"
    elif player_move.lower() == "scissors" and Ai_move.lower() == "paper":
        winner = "You Win!"
    elif player_move == Ai_move:
        winner = "You Draw"
    else:
        winner = "You lose!!!"  
    
    print(winner)
    
    while True:
        user_input = input("Do you want to play another? (Yes or No)")
    
        if user_input.lower() == "yes":
            print("Good luck then!")
            winner = "test" 
            play_game_flag = True 
            break
        elif user_input.lower() == "no":
            print("Was fun playing!")
            play_game_flag = False 
            break
        else: 
            print("I did not quite catch that? Do you want to play another?")
    
        

  
        

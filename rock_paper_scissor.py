import random
def start_game():
    print("Welcome to the game!!")
    
def rock_paper_scissors():
    start_game()
    draw=0
    user_win=0
    computer_win=0
    
    while True:
        computer=random.choice(['rock','paper','scissors'])
        ask_user=input("Do you want to play(p) or exit(e)? :")
        if ask_user=='p':
            print("Enjoy the game!")
        elif ask_user=='e':
            break
        else:
            print("Invalid input!! please try again enter (p)/(e)")
            break
            
        try:
            user_input=input("Enter either rock, paper or scissors :")
            if user_input==computer:
                draw+=1
                print(f"Draw {draw} times")
                break
            if user_input=='rock':
                print(f"computer choose {computer}")
                if computer=='scissors':
                    user_win+=1
                    print(f"You have win {user_win} times.")
                    
                else:
                    computer_win+=1
                
            if user_input=='paper':
                print(f"computer choose {computer}")
                if computer=='rock':
                    user_win+=1
                    print(f"You have win {user_win} times.")
                else:
                    computer_win+=1
            
            if user_input=='scissors':
                print(f"computer choose {computer}")
                if computer=='paper':
                    user_win+=1
                    print(f"You have win {user_win} times.")
                else:
                    computer_win+=1
        except:
            print("Program is not working")
        print(f"computer won {computer_win} times.") 
rock_paper_scissors()
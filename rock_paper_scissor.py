import random
def start_game():
    print("Welcome to the game!!")
    
def rock_paper_scissors():
    start_game()
    user_win=0
    computer_win=0
    
    while True:
        ask_user=input("Do you want to play(p) or exit(e)? :")
        if ask_user=='p':
            print("Enjoy the game!")
            
        else:
            break
        
        round=int(input("How many round do you want to play? :"))
        for i in range(1,round+1):
            computer=random.choice(['rock','paper','scissors'])
            try:
                user_input=input("Enter either rock, paper or scissors :")
            
                if user_input==computer:
                    continue
                
                if user_input=='rock':
                    print(f"computer choose {computer}")
                    if computer=='scissors':
                        user_win+=1
                        # print(f"You have win {user_win} times.")
                    else:
                        computer_win+=1
                        # print(f"computer won {computer_win} times.") 
                
                if user_input=='paper':
                    print(f"computer choose {computer}")
                    if computer=='rock':
                        user_win+=1
                        # print(f"You have win {user_win} times.")
                    else:
                        computer_win+=1
                        # print(f"computer won {computer_win} times.") 
            
                if user_input=='scissors':
                    print(f"computer choose {computer}")
                    if computer=='paper':
                        user_win+=1
                        # print(f"You have win {user_win} times.")
                    else:
                        computer_win+=1
                        # print(f"computer won {computer_win} times.") 
            except:
                print("Program is not working")
        if user_win==computer_win:
            print("Its draw")
        elif user_win>computer_win:
            print("User win")
        else:
            print("computer win")        
rock_paper_scissors()
import random
def play():
    computer_score = 0
    human_score = 0
    match_tie = 0
    lim = 0
    try:
        while lim < 10:
            com_choice  = random.choice(['r','p','s'])
            print("------------------") 
            your_choice = input("Enter your choice(r, p or s): ")
            print("------------------")
            if your_choice == com_choice:
                print("Match tie!")
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
                match_tie += 1
            elif  your_choice == 'r' and com_choice == 'p':
                print("Computer won")
                computer_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            elif your_choice == 'p' and com_choice == 's':
                print("Computer won")
                computer_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            elif your_choice == 's' and com_choice == 'r':
                print("Computer won")
                computer_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            elif  your_choice == 'p' and com_choice == 'r':
                print("You won")
                human_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            elif your_choice == 's' and com_choice == 'p':
                print("You won")
                human_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            elif your_choice == 'r' and com_choice == 's':
                print("You won")
                human_score +=1
                print(f"Computer score: {computer_score}")
                print(f"Your score: {human_score}")
            else:
                print("[!]Invalid Choice!")
                continue
            lim += 1
    except KeyboardInterrupt:
        print("")
        print("[!]Keyboard has been Interrupted!")
    except ValueError:
        print("")
        print("[!]Invalid value!")
    if human_score > computer_score:
        print("--------------------------")
        print("Congrates! You have won.")
        print("Final score is: ")
        print(f"Your Score: {human_score}")
        print(f"Computer Score: {computer_score}")
        print(f"Match Draw: {match_tie}")
        print("--------------------------")
    elif human_score <  computer_score:
        print("--------------------------")
        print("Sorry! You have lost.")
        print("Final score is: ")
        print(f"Your Score: {human_score}")
        print(f"Computer Score: {computer_score}")
        print(f"Match Draw: {match_tie}")
        print("--------------------------")    
    else:
        print("--------------------------")
        print("Sorry! Match Draw.")
        print("Final score is: ")
        print(f"Your Score: {human_score}")
        print(f"Computer Score: {computer_score}")
        print(f"Match Draw: {match_tie}")
        print("--------------------------")
            
    

print("##########################")
print("   ROCK-PAPER-SCISSORS     ")
print(" Dev by Rakibul Hasan Asif ")
print("##########################")
play()
while True:
    try:
        wish  = input("Do you want to play again?(y or n): ")
        if wish.lower() == 'y':
            print("##########################")
            print("   ROCK-PAPER-SCISSORS     ")
            print(" Dev by Rakibul Hasan Asif ")
            print("##########################")
            play()
        elif wish.lower() == 'n':
            print("Thanks for playing the game!")
            break
        else:
            print("[!] Invalid choice.")
    except KeyboardInterrupt:
        print("")
        print("[!]Keyboard has been Interrupted!")
    except ValueError:
        print("")
        print("[!]Invalid value!")
    
    


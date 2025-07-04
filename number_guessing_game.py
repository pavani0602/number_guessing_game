#Number Guessing Game
import random
name=input("Enter your Name : ")
games_played=1
games_won=0
def get_number():
    while True:
        try:
            num = int(input("Please enter a number from 1 to 100: "))
            if 1 <= num <= 100:
                return num
            else:
                print("🚫 Number out of range! Please enter between 1 and 100.")
        except ValueError:
            print("🚫 Invalid input! Please enter a valid whole number.")
def crackit():
    global games_won
    target_number=random.randint(1,100)
    print("Choose difficulty level:")
    print("1. Easy (5 attempts)")
    print("2. Medium (3 attempts)")
    print("3. Hard (1 attempt)")
    try:
        choice = int(input("Enter choice (1/2/3): "))
    except ValueError:
        print("Invalid input! Defaulting to Medium difficulty (3 attempts).")
        choice = 2
    if choice == 1: 
        max_attempts = 5
    elif choice == 2:
        max_attempts = 3
    elif choice == 3:
        max_attempts = 1
    else:
        print("Invalid input! Defaulting to Medium difficulty (3 attempts).")
        max_attempts = 3 
    attempts_used=1
    user_number=get_number()
    if user_number==target_number:
        print("Woah! You cracked it In jus one GO Great!")
        games_won=games_won+1
        return
    while target_number!=user_number :
        if attempts_used==max_attempts:
            print("Limit Over!")
            print("The number was "+str(target_number))
            break
        if user_number>target_number:
            if abs(user_number - target_number) <= 5:
                print("Too Close!")
            else:
                print("Too High")
        else:
            if abs(user_number - target_number) <= 5:
                print("Too Close!")
            else:
                print("Too Low")
        user_number=get_number()
        attempts_used=attempts_used+1
    if(target_number==user_number) :
        if attempts_used==2:
            print('Wow, you cracked it just At 2nd Attempt')
            games_won=games_won+1
        else:
            print("Woah!,you got it after trying for " + str(attempts_used) + " times")
            games_won=games_won+1
crackit()
play_again=input("Do you want to try again?(YES/NO): ").strip().upper()
while play_again=="YES":
    games_played=games_played+1
    crackit()
    play_again=input("Do you want to try again?(YES/NO): ").strip().upper()
print(f"You Played {games_played} Time{'s' if games_played > 1 else ''}! And You won {games_won} Time{'s' if games_won != 1 else ''}!")
print("Thanks for Playing "+ name + "!")
input("Please Enter to Exit")

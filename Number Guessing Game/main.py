import art
import random
print(art.logo)

NUMBER=random.randint(0,100)

def play_game(lives,NUMBER):
    guess= -1
    print(f"You have {lives} attempts to guess number between 0 and 100 :")
    while lives>0:
        guess=int(input("Enter the number :"))
        if guess < NUMBER :
            if NUMBER-guess <=5:
                print("Close but low")
                lives-=1
                print(f"{lives} attempts are left!!!!")
            else:    
                print("Too Low!!!")
                lives-=1
                print(f"{lives} attempts are left!!!!")
        elif guess > NUMBER :
            if guess-NUMBER <=5:
                print("Close but high")
                lives-=1
                print(f"{lives} attempts are left!!!!")
            else:
                print("Too High!!!")
                lives-=1
                print(f"{lives} attempts are left!!!!") 
        else:
            print(f"You guessed the number {NUMBER} !!!")
            break
    if lives==0:
        print(f"You lost to guess the number {NUMBER}!!!")

choice=input("Do you wanna play a number guessing game : Yes or No :").lower()
if choice =='yes':
    choice=input("Hard or Easy :").lower()
    if choice=='hard':
        play_game(5,NUMBER)
    elif choice=="easy":
        play_game(10,NUMBER)
    else:
        print("Invalid Input")
                    
else:
    print("Goodbye")
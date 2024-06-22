import random
import os
import art
import sys
from data import data

def check_choice(tempA,tempB,choice):
    global score
    if choice=='a':
            if tempA["follower_count"] > tempB["follower_count"]:
                  score+=1
                  print(f"You're right! Current Score: {score}.")
                  return False
            elif tempA["follower_count"] < tempB["follower_count"]:
                  print(f"You're Wrong! Current Score: {score}.")
                  return True
    elif choice=='b':
        if tempB["follower_count"] > tempA["follower_count"]:
                score+=1
                print(f"You're right! Current Score: {score}.")
                return False
        elif tempB["follower_count"] < tempA["follower_count"]:
                print(f"You're Wrong! Current Score: {score}.")     
                return True
    else:
        print("Invalid Choice")
        return True
                
def play_game():   
    is_wrong=False
    global score
    tempA=random.choice(data) #to intialize the tempA only one time because other times tempA = TempB
    while not is_wrong:
        print(art.logo)
        print(f"Current Score = {score}.")
        tempB=random.choice(data)
        print(f"Compare A: {tempA["name"]}, a {tempA["description"]}, from {tempA["country"]}.")
        print(art.vs)
        print(f"Compare B: {tempB["name"]}, a {tempB["description"]}, from {tempB["country"]}.")
        choice=input("Who has more followers? Type A or B :").lower()
        if choice=='areeba':# a fun condition just for peach
            os.system("cls")
            print("All hands down to the greatest player. You win!!!")
            sys.exit()
        is_wrong=check_choice(tempA,tempB,choice)
        if is_wrong==True:
            break
        else:
            tempA=tempB
            tempB=random.choice(data)
            os.system("cls")
score=0             
play_game()
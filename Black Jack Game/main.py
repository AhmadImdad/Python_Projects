import random
import sys
from art import logo
print(logo)
choice1 = input("Do you want to play Blackjack? Yes or No: ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if choice1 == 'yes':
    # Initialize user and computer hands
    user_cards = []
    computer_cards = []
    
    # Deal initial cards
    for _ in range(2):
        user_card = random.choice(cards)
        user_cards.append(user_card)
        computer_card = random.choice(cards)
        computer_cards.append(computer_card)
    
    # Print initial cards
    print("Your cards are:", user_cards)
    print("Computer's first card is:[", computer_cards[0],"]")
    
    # Check for natural blackjack
    if sum(user_cards) == 21 and sum(computer_cards)!=21:
        print("Natural Blackjack! You win!")
        sys.exit()
    elif sum(computer_cards) == 21 and sum(user_cards) != 21:
        print("Computer has a Natural Blackjack. You lose!")
        sys.exit()
    elif sum(computer_cards) == 21 and sum(user_cards) == 21:
        print("DRAW!!!")
        sys.exit()
        
    
    # User's turn
    while True:
        choice2 = input("Do you want another card? Yes or No: ").lower()
        if choice2 == "yes":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            print("Your cards are now:", user_cards)
            if sum(user_cards) > 21 and 11 in user_cards:
                # If user busts and has an Ace counted as 11, change it to 1
                user_cards[user_cards.index(11)] = 1
                print("Changed Ace value from 11 to 1")
            elif sum(user_cards) > 21:
                print("Bust! You lose!")
                sys.exit()
        else:
            break
    
    # Computer's turn
    while sum(computer_cards) <= 16:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        print("Computer's cards are now:", computer_cards)
        if sum(computer_cards) > 21 and 11 in computer_cards:
            # If computer busts and has an Ace counted as 11, change it to 1
            computer_cards[computer_cards.index(11)] = 1
            print("Changed Ace value from 11 to 1")
        elif sum(computer_cards) > 21:
            print("Computer busts! You win!")
            sys.exit()
    
    # Compare hands
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    
    print(f"Your sum = {user_sum} and Computer's Sum = {computer_sum}")
    
    if user_sum > computer_sum:
        print(computer_cards," are computer cards.")
        print(user_cards," are your cards.")
        print("You win!")
    elif user_sum < computer_sum:
        print(computer_cards," are computer cards.")
        print(user_cards," are your cards.")
        print("Computer wins!")
    else:
        print(computer_cards," are computer cards.")
        print(user_cards," are your cards.")
        print("It's a draw!")
    
else:
    print("Goodbye!")

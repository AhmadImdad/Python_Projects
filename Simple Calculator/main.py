import os
import art
def add(n1,n2):
    """adds two numbers"""
    return n1+n2
def subtract(n1,n2):
    """subtracts two numbers"""
    return n1-n2
def multiply(n1,n2):
    """multiply two numbers"""
    return n1*n2
def divide(n1,n2):
    """Divides two numbers"""
    return n1/n2
def calculator(choice1):
    for i in operators:
        print(i)
    choice2=input("Enter the operation: ")
    choice3=float(input("Enter the second number: "))
    if choice2=='*':
        result=multiply(choice1,choice3)
        print(f"{choice1} * {choice3} = {result}")
    elif choice2=='/':
        result=divide(choice1,choice3)
        print(f"{choice1} / {choice3} = {result}")
    elif choice2=='+':
        result=add(choice1,choice3)
        print(f"{choice1} + {choice3} = {result}")
    elif choice2=='-':
        result=subtract(choice1,choice3)
        print(f"{choice1} - {choice3} = {result}")
    choice4=input("Do you want to do more calcution on this one: Yes or No :").lower()
    if(choice4=='yes'):
        calculator(result)
    else:
        return
while True:
    print(art.logo)
    choice1=input("Enter the First number:")
    operators=['*','/','-','+']
    calculator(float(choice1))
    os.system("cls")
    

import random
import graphics
import os
import word_list
choice=1
while choice==1:
    os.system("cls")
    size_of=len(word_list.word_list)
    word_index=random.randint(0,size_of)
    word=word_list.word_list[word_index]
    lives=6
    blank=list()
    flag=list()
    record=0
    for i in range (len(word)):
            blank.append("_")
            flag.append(0)
    while True:
        print(graphics.logo)
        check=False
        print(" ".join(blank))
        result="".join(blank)
        if lives!=0:
            record1=(lives+record)% 6
            print(graphics.stages[record1])
        if(result==word):
            print("You won!!!") 
            choice=int(input("If you wanna play again, press 1, otherwise press any button: "))
            break
        elif lives ==0:
             print(graphics.stages[6]) 
             print("You lost!!!")
             print(f"Word is {word_list.word_list[word_index]}!!!.")
             choice=int(input("If you wanna play again, press 1, otherwise press any button: "))
             break
        alphabet=input("Enter an alphabet:").lower()
        for i in range(len(word)):
              if alphabet==word[i] and flag[i]==0:
                 blank[i]=alphabet
                 flag[i]=1
                 check=True
        if check== False:
            lives-=1
            record+=2
        os.system("cls")
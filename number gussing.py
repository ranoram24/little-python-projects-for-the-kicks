import random as rand
import time
i=['Y','N']
print("welcome!")
while True:
    print("enter a start and finish point to the number")
    while True:
        try:
            a=int(input("start: "))
            b=int(input("finish: "))
            while a>b:
                print("start cant be larger then finish, try again")
                a=int(input("start: "))
                b=int(input("finish: "))
            break
        except:
            print("only an int please!")
    
    print("computer thinking of a number....")
    time.sleep(3)
    comp_choice=rand.randint(a,b)
    chances=7
    print("now guess a number between ",a,"and ",b)
    while chances>0:
        print("you have",chances,"chances left!")
        while True:
            try:
                player_choice=int(input("your guess: "))
                while player_choice<a or player_choice>b:
                    print("not between the range. we let you go with this one\n try again:")
                    player_choice=int(input("your guess: "))
                break
            except:
                print("not a valid intiger! we let you go with this one. try again!")
                


        if player_choice==comp_choice:
            print("you win! the number was indeed",player_choice)
            break
        elif player_choice>comp_choice:
            print("number is smaller then your guess")
        elif player_choice<comp_choice:
            print("number is larger then your guess")
        chances-=1
        if chances==0:
            print("your out of chances! you lose!\n the number was",comp_choice)

    print("try again? Y/N")
    ch=input()
    while ch.upper() not in i:
        print("invalid choice,try again!")
        ch=input()
    if ch.upper()=='N':
        break
    
    
    
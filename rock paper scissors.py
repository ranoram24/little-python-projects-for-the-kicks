import random as rand
import time
options=['rock','paper','scissors']
comp_choice=rand.choice(options)
i=['Y','N']
result_map = {
    ('rock', 'scissors'): ' player win',
    ('rock', 'paper'): ' player lose',
    ('rock', 'rock'): 'draw',
    ('paper', 'rock'): 'player win',
    ('paper', 'scissors'): ' player lose',
    ('paper', 'paper'): 'draw',
    ('scissors', 'paper'): 'player win',
    ('scissors', 'rock'): 'player lose',
    ('scissors', 'scissors'): 'player draw'
}

print("WELCOME!")
while True:
    print("CHOOSE OPTIONS\n 1-:",options[0], "\n 2-:",options[1], "\n 3-:",options[2])

    while True:
     try:
            player_choice=int(input("player choice:"))
            while player_choice<1 or player_choice>3:
                print("choose between this options only! try again")
                print("1-:",options[0], "\n 2-:",options[1], "\n 3-:",options[2])
                player_choice=int(input("player choice:"))
            break
     except:
            print("choose only a number!")
            print("1-:",options[0], "\n 2-:",options[1], "\n 3-:",options[2])

    player_choice_str=options[player_choice-1]
    print("your choice is: ",player_choice_str)
    print("comp_choice is: ",comp_choice)
    print(result_map[(player_choice_str,comp_choice)])
    print("play again? Y/N")
    continu=input()
    while continu.upper() not in i:
        print("invalid choice try again")
        continu=input()
    if continu.upper()=='N':
        break



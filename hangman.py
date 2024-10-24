import random
from collections import Counter
#list of words to choose from
superhero_movies = [
    "hulk",
    "thor",
    "superman",
    "aquaman",
    "shazam",
    "blade",
    "catwoman",
    "zorro",
    "hellboy",
    "spawn",
    "batman",
    "flash",
    "antman",
    "deadpool",
    "daredevil",
    "kick-ass",
    "watchmen",
    "skyfall",
    "jumper",
    "morbius",
    "venom",
    "eternals",
    "incredibles",
    "birdman",
    "chronicle",
    "megamind",
    "brightburn",
    "underdog",
    "ghostbusters",
    "zoom"
]
#a game loop that restart at every game
while True:
    #choosing a word at random and setting up the game
    chosen_word=random.choice(superhero_movies)

    print("GUESS THE WORD! HINT: A SUPERHERO MOVIE")
    for i in range(len(chosen_word)):
        print('_',end='')
    print()
    #a string that holds the letter guessed, how many chances, how many we did correct and a flag that we did it
    letter_guessed=''
    chances=len(chosen_word)+2
    correct=0
    flag=0
    try:
        #as long as we didnt complete the word
        while chances!=0 and flag==0:
            print("guess!")
            chances-=1
            try:
                guess=str(input("enter guessed letter:"))
            except:
                print("input only a letter")
            
            if not guess.isalpha():
                print("enter only a letter!") #numbers not included
                continue
            elif len(guess)>1:
                print("only ONE letter")#the game rules
                continue
            elif guess in letter_guessed:
                print("already guessed that letter")#giving a prompt
                continue
            if guess in chosen_word: 
                k=chosen_word.count(guess)
                for _ in range(k):
                    letter_guessed+=guess #adding the number of time the letter in the words
            
            for char in chosen_word:
                #if you got some. the current is rising. if the number of letter is equal you won the game and exit
                if char in letter_guessed and Counter(letter_guessed)!=Counter(chosen_word):
                    print(char,end='')
                    correct+=1 
                    
                elif Counter(letter_guessed)==Counter(chosen_word):
                    print(f"the word is {chosen_word}",end='')
                    flag=1
                    print("")
                    print("YOU WON!")
                    break
                    
                else:
                    print('_',end='')
        if chances<=0 and Counter(letter_guessed)!= Counter(chosen_word):
            print()
            print(f"you lost! the word was {chosen_word}")
        print("wanna play again? Y/N")
        choice=input()
        while choice.lower()!='y' and choice.lower()!='n':
            print("invalid choice")
            choice=input()
        if choice.lower()=='n':
            break


    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
    

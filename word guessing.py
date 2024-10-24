import random

print("what is your name?")
name=input("name: ")
print(f"good luck {name}!")
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
while True:
    chosen_word=random.choice(superhero_movies)
    guesses=''
    turns=12
    while turns>0:
        print("guess a character:",end=' ')
        ug=input()
        guesses+=ug
        failed=0
        for char in chosen_word:
        
            if char in guesses:
                print(char,end='')
            else:
                print("_",end='')
            
                failed+=1
        if failed==0:
            print(f"you win! the word was {chosen_word}")
            break
        else:
            turns-=1
    if turns==0:
        print(f"you lose, the word was {chosen_word}")
    print("wanna play again? Y/N")
    choice=input()
    while choice.lower()!='y' and choice.lower()!='n':
        print("invalid choice")
        choice=input()
    if choice.lower()=='n':
        break
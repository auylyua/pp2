import random 
def guess():
    t = random.randint(1, 20)
    name = input("Hello! What is your name?")
    print(f"""Well,{name}, I am thinking of a number between 1 and 20.
Take a guess.""")
    a=0
    while True: 
        n=int(input())
        a+=1
        if n > t: 
            print("Your guess is too high.\nTake a guess.") 
        elif n < t: 
            print("Your guess is too low.\nTake a guess.")
        else: 
            print(f"Good job, {name}! You guessed my number in {a} guesses!")
            break
        
guess()
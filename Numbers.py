import random

print("Number Guessing Game")
print("Guess a Number (Between 1 and 9)")

number = random.randint(1,9)

count = 0
while count < 5:
    guess = int(input("Enter Your Guess:- "))

    if guess == number:
        print("Congratulations You WON!!")

    elif guess < number:
        print("Your Guess Was Too Low, Guess a Number Higher Than ",guess)    
    else:
        print("Your Guess Was Too High, Guess a Number Lower Than ",guess)

    count = count+1    

if not count < 5:
    print("YOU LOST!, The number is ",number)
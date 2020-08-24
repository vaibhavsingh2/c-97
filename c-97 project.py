import random
print("Guess the number")

number = random.randint(1, 10)

chance = 0

print("Guess a number between 1 and 10:")

while chance < 5:
    guess=int(input("Write your guess: "))

    if guess == number:
        
        print("You have won")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)


    chance+=1

    if not chance < 5:

        print("YOU LOSE!!! The number is", number)
        





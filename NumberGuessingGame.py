import random

while True:
    print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")

    for i in range(1):
        answer = random.randrange(1, 10)
        guess = int(input("Enter your first guess: "))
        if guess == answer:
            print("You win!")
            break
        elif guess > answer:
            print("Your guess is too high.")
        elif guess < answer:
            print("Your guess is too low.")
        guess = int(input("Enter your second guess: "))
        if guess == answer:
            print("You win!")
            break
        elif guess > answer:
            print("Your guess is too high.")
        elif guess < answer:
            print("Your guess is too low.")
        guess = int(input("Enter your third guess: "))
        if guess == answer:
            print("You win!")
            break
        elif guess > answer:
            print("Your guess is too high.")
        elif guess < answer:
            print("Your guess is too low.")
        print("You lose. The number was " + str(answer))
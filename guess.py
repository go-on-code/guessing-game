from random import randint


def main():
    print("Welcome to the number guessing game!")
    number = randint(1, 100)
    while True:
        guess = input("Guess a number between one and 100:  ")
        if int(guess) == number:
            print("That is right!")
            break
        elif int(guess) > number:
            print("Sorry, that's to high. Guess again please!")
        elif int(guess) < number:
            print("Sorry that is to low. Guess again!")


if __name__ == '__main__':
    main()
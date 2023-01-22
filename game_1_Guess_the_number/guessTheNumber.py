'''
1. Change the number range from 1 to 1000
2. Game should ask us to guess the number
3. Gime a clue of the number is higher or lower than guess
4. Inform the player of he won

'''

from random import randint

start = 1
end = 1000

value = randint(start, end)

print("The computer choose a number between ", start, "and ", end )

guess = None

while guess != value:
    guess = int(input("Guess the number: "))

    if guess < value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")
print("Congratulations!!! You guess the number. You won. ")
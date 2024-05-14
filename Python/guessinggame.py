# secret_number = 7
# guess_count = 0
# while guess_count < 3:
#     guess= int(input("guess a number(1-10): "))
#     guess_count += 1
#     if guess ==secret_number:
#         print("congratulation, you guessed it!")
#         break
#     else:
#         print("try again")

# if guess_count ==3:
#     print("sorry, you ran out of guesses, The number was",secret_number)




# guessing_game()
import random

min_number = 1
max_number = 5

secret_number = (random.randint(min_number, max_number))

print("Welcome to the Guessing Game!")
print(f"I'm thinking of a number between {min_number} and {max_number}. Can you guess it?")

while True:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break

# import random

# secret_number = random.randint(1,5)
# guess_count = 0
# # max_guesses = 2
# while guess_count < 3:
#     guess = int(input("Guess any number betweeen 1-5: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("congratulation, you guessed it!")
#         break
#     else: 
#         print("try again")

# if guess_count == 3:
#     print(f"sorry, you ran out of guesses, The number was {secret_number}!")































































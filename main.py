# import random
#
# levels = {"easy": 10, "hard": 5}
# number_range = random.randint(1, 100)
# #print(number_range)
#
# print ("Welcome to the number guessing game!")
# print("I'm thinking of a number between 1 and 100")
# choosen_level = input(f"Choose a difficultly. Type 'easy' or 'hard': ").lower()
#
# if choosen_level == 'easy':
#     level_chosen = levels["easy"]
#     print("You have 10 attempts remaining to guess the number")
#
#     while level_chosen != 0:
#         guess = int(input("make a guess "))
#         if guess != number_range:
#             level_chosen -= 1
#             print(f"You have {level_chosen} attempts remaining to guess the number")
#             if guess < number_range:
#                 print("You are to low")
#             else:
#                 print("You are to high")
#         else:
#             print("You got it right!")
#             break
#
# elif choosen_level == 'hard':
#     level_chosen = levels["hard"]
#     print(f"You have {level_chosen} attempts remaining to guess the number")
#
#     while level_chosen != 0:
#         guess = int(input("make a guess "))
#         if guess != number_range:
#             level_chosen -= 1
#             print(f"You have {level_chosen} attempts remaining to guess the number")
#             if guess < number_range:
#                 print("You are to low")
#             else:
#                 print("You are to high")
#         else:
#             print("You got it right!")
#             break

import random

def play_game(attempts):
    number_range = random.randint(1,100)
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == number_range:
            print("You got it right! 🎉")
            return
        attempts -+ 1
        print(f"You have {attempts} attempts remaining.")
        if guess < number_range:
            print("You are too low.")
        else:
            print("You are too high.")

        if attempts == 0:
            print(f"Out of attempts! The number was {number_range}. Better luck next time!")

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
levels = {"easy": 10, "hard": 5}

chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if chosen_level in levels:
    play_game(levels[chosen_level])
else:
    print("Invalid choice. Please restart and choose 'easy' or 'hard'.")

from random import randint

print("Welcome to Rock Paper Scissors Game!")


def r_p_s():
    global user_input, computer_input

    if user_input < 0 or user_input > 2:
        return ("Invalid choice please enter right option")
    elif user_input == computer_input:
        return ("Match Drawn.")
    elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (
            user_input == 2 and computer_input == 0):
        return ("You WIN!!!!!!!!")
    else:
        return ("You Lose.")


# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice = {0: rock, 1: scissors, 2: paper}
names = {0: "Rock", 1: "Scissors", 2: "Paper"}
user_input = int(input("Enter 0 for Rock, 1 for Scissors and 2 for Paper.\n"))
computer_input = randint(0, 2)
try:
    print(
        f"You chose {names[user_input]}\n{choice[user_input]}\nComputer chose {names[computer_input]}\n{choice[computer_input]}")
except KeyError:
    pass

print(r_p_s())

import random
from tkinter import messagebox


def probability_event():
    return random.random()


def move_check(player_choice, computer_choice, windowgame, show_start_window):
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"You chose: {player_choice.upper()}\nComputer chose: {computer_choice.upper()}\n\n{result}")
    retry = messagebox.askyesno("Play Again?", "Do you want to try again?")
    if retry:
        windowgame.withdraw()
        show_start_window()
    else:
        windowgame.destroy()


def diff_easy(player_choice, windowgame, show_start_window):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    move_check(player_choice, computer_choice, windowgame, show_start_window)


def diff_normal(player_choice, windowgame, show_start_window):
    choices = ["rock", "paper", "scissors"]
    prob = probability_event()
    if prob <= 0.35:
        computer_choice = random.choice(choices)
    else:
        if player_choice == "rock":
            computer_choice = "paper"
        elif player_choice == "paper":
            computer_choice = "scissors"
        else:
            computer_choice = "rock"
    move_check(player_choice, computer_choice, windowgame, show_start_window)


def diff_hard(player_choice, windowgame, show_start_window):
    choices = ["rock", "paper", "scissors"]
    prob = probability_event()
    if prob <= 0.1:
        computer_choice = random.choice(choices)
    else:
        if player_choice == "rock":
            computer_choice = "paper"
        elif player_choice == "paper":
            computer_choice = "scissors"
        else:
            computer_choice = "rock"
    move_check(player_choice, computer_choice, windowgame, show_start_window)


def diff_impossible(player_choice, windowgame, show_start_window):
    if player_choice == "rock":
        computer_choice = "paper"
    elif player_choice == "paper":
        computer_choice = "scissors"
    else:
        computer_choice = "rock"

    if player_choice == computer_choice:
        result = "It's a tie!? How did you even manage that?!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "paper") or \
        (player_choice == "paper" and computer_choice == "rock"):
        result = "You won?! Suspicious..."
    else:
        result = "You Lose! (As expected...)"

    messagebox.showinfo("Impossible Mode Result", f"You chose {player_choice.upper()}.\nComputer chose {computer_choice.upper()}.\n\n{result}")
    retry = messagebox.askyesno("Play Again?", "Do you want to try again?")
    if retry:
        windowgame.withdraw()
        show_start_window()
    else:
        windowgame.destroy()

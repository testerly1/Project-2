from tkinter import *
from random import randint
from tkinter import ttk

gameWindow = Tk()
gameWindow.title('Lets Play Rock, Paper, Scissors!')
gameWindow.geometry('600x600')
gameWindow.resizable(False, False)
gameWindow.config(bg='purple')

# Images For Game
rock = PhotoImage(file='img.png')
paper = PhotoImage(file='img_1.png')
scissors = PhotoImage(file='img_2.png')

# Images in a list
image_list = [rock, paper, scissors]

# RNG
rng_number = randint(0, 2)

# base image
image_label = Label(gameWindow, image=image_list[rng_number], bd=0, )
image_label.pack(pady=20)

comp_score = 0
player_score = 0


# creat the game
def game():
    global comp_score
    global player_score
    # RNG
    rng_number = randint(0, 2)
    # image
    image_label.config(image=image_list[rng_number])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    # words to numbers
    if player_choice.get() == "Rock":
        player_choice_value = 0
    elif player_choice.get() == "Paper":
        player_choice_value = 1
    elif player_choice.get() == "Scissors":
        player_choice_value = 2

    # player choice is rock
    if player_choice_value == 0:
        if rng_number == 0:
            player_score_label.config(text=player_score + 1)
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            player_score += 1
            win_lose_label.config(text="Game is Tied! Play Again?")
        elif rng_number == 1:
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            win_lose_label.config(text="Paper Beats Rock You Lose! Play Again?")
        elif rng_number == 2:
            player_score_label.config(text=player_score + 1)
            player_score += 1
            win_lose_label.config(text="Rock Beats Scissors You Win! Play Again?")

    # player choice is Paper
    if player_choice_value == 1:
        if rng_number == 1:
            player_score_label.config(text=player_score + 1)
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            player_score += 1
            win_lose_label.config(text="Game is Tied! Play Again?")
        elif rng_number == 0:
            player_score_label.config(text=player_score + 1)
            player_score += 1
            win_lose_label.config(text="Paper Beats Rock You Win! Play Again?")
        elif rng_number == 2:
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            win_lose_label.config(text="Scissors Beats Paper You Lose! Play Again?")

    # player choice is scissors
    if player_choice_value == 2:
        if rng_number == 2:
            player_score_label.config(text=player_score + 1)
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            player_score += 1
            win_lose_label.config(text="Game is Tied! Play Again?")
        elif rng_number == 0:
            comp_score_label.config(text=comp_score + 1)
            comp_score += 1
            win_lose_label.config(text="Rock Beats Scissors You Lose! Play Again?")
        elif rng_number == 1:
            player_score_label.config(text=player_score + 1)
            player_score += 1
            win_lose_label.config(text="Scissors Beats Paper You Win! Play Again?")


def reset():
    global comp_score
    global player_score
    comp_score = 0
    player_score = 0
    comp_score_label.config(text=comp_score)
    player_score_label.config(text=player_score)



# choice
player_choice = ttk.Combobox(gameWindow, value=("Rock", "Paper", "Scissors"))
player_choice.current(0)
player_choice.pack(pady=20)

# game button
game_button = Button(gameWindow, text="Play!", command=game)
game_button.pack(pady=10)

# reset button
reset_button = Button(gameWindow, text="Reset!", command=reset)
reset_button.pack(pady=10)

# win or lose
win_lose_label = Label(gameWindow, text="", font=("Adobe Garamond Pro Bold", 20), bg="#856ff8")
win_lose_label.pack(pady=50)

# player label
players_score_label = Label(gameWindow, text='Player Score', font=("Adobe Garamond Pro Bold", 20), bg="#856ff8")
players_score_label.pack(padx=0)

player_score_label = Label(gameWindow, text='', font=("Adobe Garamond Pro Bold", 20), bg="#856ff8")
player_score_label.pack(padx=0)

# computer score
comps_score_label = Label(gameWindow, text='Computer Score', font=("Adobe Garamond Pro Bold", 20), bg="#856ff8")
comps_score_label.pack(padx=0)

comp_score_label = Label(gameWindow, text='', font=("Adobe Garamond Pro Bold", 20), bg="#856ff8")
comp_score_label.pack(padx=0)

gameWindow.mainloop()

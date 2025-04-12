import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Label
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap import Window
from ttkbootstrap.icons import Icon
import os
from PIL import Image, ImageTk, ImageFont
import tkinter.font as tkFont
from PIL import ImageDraw
import sys


#Main Window 
root = Window(themename='darkly')
root.withdraw()
windowstart = Toplevel(root)
windowstart.title("Simple Rock, Paper, Scissors!")
windowstart.geometry('800x400')
windowstart.tk.call('tk', 'scaling', 2.0)

#Game Window
windowgame = Toplevel(root)
windowgame.withdraw()
windowgame.title("Enter your choice (rock, paper, scissors): ")
windowgame.geometry('800x400')
windowgame.tk.call('tk', 'scaling', 2.0)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def rps_play(player_choice):
    selected = diffopt.get()
    if selected == "easy":
        diff_easy(player_choice)
    elif selected == "normal":
        diff_normal(player_choice)
    elif selected == "hard":
        diff_hard(player_choice)
    elif selected == "impossible":
        diff_impossible(player_choice)

def set_difficulty(level):
    diffopt.set(level)
    windowstart.withdraw()
    setup_game_buttons()
    windowgame.deiconify()

def setup_game_buttons():                               #WHY CAN'T SHIT BE SIMPLE FFS
    for widget in windowgame.winfo_children():
        widget.destroy()
    ttk.Label(windowgame, text="Choose your move:").pack(pady=10)
    ttk.Button(windowgame, text="Rock", command=lambda: rps_play("rock")).pack()
    ttk.Button(windowgame, text="Paper", command=lambda: rps_play("paper")).pack()
    ttk.Button(windowgame, text="Scissors", command=lambda: rps_play("scissors")).pack()
    global result_label
    result_label = ttk.Label(windowgame, text="", font="Calibri 12", padding=10)
    result_label.pack()

def rps(selected_diff):
    difficulty_map = {
        "easy": diff_easy,
        "normal": diff_normal,
        "hard": diff_hard,
        "impossible": diff_impossible
    }
    difficulty_map[selected_diff]()

def probability_event():
    return random.random()

def move_check(player_choice, computer_choice):                             #NIGGA THIS TOOK ME 2 HOURS TO FIGURE OUT
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

def diff_easy(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    move_check(player_choice, computer_choice)

def diff_normal(player_choice):
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
    move_check(player_choice, computer_choice)

def diff_hard(player_choice):
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
    move_check(player_choice, computer_choice)

def diff_impossible(player_choice):
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

def show_start_window():
    global diffopt
    diffopt.set("")
    windowstart.deiconify()


##GUI ELEMENTS##

#title
title_label = ttk.Label(master = windowstart, text = 'Welcome to Simple Rock, Paper, Scissors!', font = 'Calibri 18 bold')
title_label.pack()

title_label2 = ttk.Label(master = windowstart, text = 'Choose your Difficulty (Scales exponentially with each step)', font = 'Calibri 14')
title_label2.pack()

#font and style params
font_path = "C:/Windows/Fonts/segoeui.ttf"
bold_font = ImageFont.truetype(font_path, size=10)

boldstyle = Style()
boldstyle.configure("HoverStyle.TButton", font=("Segoe UI", 10, "bold"),borderwidth=0, focusthickness=1, background='', focuscolor="none", padding=6, relief='flat')

boldstyle.map(
    "HoverStyle.TButton",
    font=[("active", bold_font)],
    foreground=[("active", "white")],
    background=[("active", "")],
    relief=[("active", "flat")],
)
#image directory 1
script_dir = os.path.dirname(os.path.abspath(__file__))
easyimg_path = resource_path("assets/easy.png")
normalimg_path = resource_path("assets/normal.png")
hardimg_path = resource_path("assets/hard.png")
impossimg_path = resource_path("assets/impossible.png")
normalbtn = resource_path("assets/btn_normal.png")
hoverbtn = resource_path("assets/btn_hover.png")
splashimg_path = resource_path("assets/splashimage.png")
rockimg_path = resource_path("assets/rock.png")
paperimg_path = resource_path("assets/paper.png")
scissorsimg_path = resource_path("assets/scissors.png")

#resizing images for buttons FFSSSSSSSSSSSSSSSS 2
imgeasy_re = Image.open(easyimg_path).resize((40, 40))
imgnormal_re = Image.open(normalimg_path).resize((40, 40))
imghard_re = Image.open(hardimg_path).resize((40, 40))
imposs_re = Image.open(impossimg_path).resize((40, 40))
normalbtn_re = Image.open(normalbtn).resize((180,60), Image.LANCZOS)
hoverbtn_re = Image.open(hoverbtn).resize((180,60), Image.LANCZOS)
rockimg_re = Image.open(rockimg_path).resize((150, 150))
paperimg_re = Image.open(paperimg_path).resize((150, 150))
scissorsimg_re = Image.open(scissorsimg_path).resize((150, 150))
splashimg_re = Image.open(splashimg_path).resize((250, 250)).convert("RGBA")
background = Image.new("RGBA", splashimg_re.size, (30, 30, 30, 255))  # RGB for #1e1e1e
flattened = Image.alpha_composite(background, splashimg_re)

#images haha 3
easyimg = ImageTk.PhotoImage(imgeasy_re)
root.easyimg = easyimg 
normalimg = ImageTk.PhotoImage(imgnormal_re)
root.normalimg = normalimg
hardimg = ImageTk.PhotoImage(imghard_re)
root.hardimg = hardimg
impossimg = ImageTk.PhotoImage(imposs_re)
root.impossimg = impossimg
normalbtnimg = ImageTk.PhotoImage(normalbtn_re)
root.normalbtnimg = normalbtnimg
hoverbtnimg = ImageTk.PhotoImage(hoverbtn_re)
root.hoverbtnimg = hoverbtnimg
rockimg = ImageTk.PhotoImage(rockimg_re)
root.rockimg = rockimg
paperimg = ImageTk.PhotoImage(paperimg_re)
root.paperimg = paperimg
scissorsimg = ImageTk.PhotoImage(scissorsimg_re)
root.scissorsimg = scissorsimg
splashimg = ImageTk.PhotoImage(splashimg_re)
root.splashimg = splashimg

#Splash Image :D
splash_canvas = tk.Canvas(windowstart, width=300, height=300, bg="#ffffff", bd=0, highlightthickness=0)
splash_canvas.place(x=480, y=100)
splash_img_obj = splash_canvas.create_image(0, 0, anchor="nw", image=root.splashimg)

float_direction = 1
#floaty anims
def float_splash():
    global float_direction
    coords = splash_canvas.coords(splash_img_obj)
    y = coords[1] + float_direction
    splash_canvas.coords(splash_img_obj, coords[0], y)
    if y <= 0 or y >= 10:
        float_direction *= -1
    windowstart.after(75, float_splash)

float_splash()


#IDK WTF but experimenting with combining button img and the bg
combined = normalbtn_re.copy()
draw = ImageDraw.Draw(combined)
draw.text((60, 10), "Easy", font=bold_font, fill="white")
combined.paste(imgeasy_re, (10, 0), imgeasy_re)
easyfinal_img = ImageTk.PhotoImage(combined)
root.easyfinal_img = easyfinal_img

#CANVAS STUFF
# Canvas dimensions
btn_width = 240
btn_height = 80
btn_x = 100
btn_y = 100

# Create canvas
def create_canvas_button(master, x, y, bg_image, icon_image, text, command, hover_image=None, width= 140):
    canvas = tk.Canvas(master, width=240, height=80, highlightthickness=0, bg="black", bd=0)
    canvas.place(x=x, y=y)
    bg =canvas.create_image(0, 0, image=bg_image, anchor="nw", tags="bg")
    icon = canvas.create_image(5, 30, image=icon_image, anchor="w")
    label = canvas.create_text(50, 30, text=text, anchor="w", font=("Segoe UI", 10, "bold"), fill="white")
    canvas.bind("<Button-1>", lambda e: command())
    def on_enter(event):
        canvas.config(cursor="hand2")
        if hover_image:
            canvas.itemconfig(bg, image=hover_image)

    def on_leave(event):
        canvas.config(cursor="")
        canvas.itemconfig(bg, image=bg_image)
    
    def on_click(event):
        command()

    # Bind to canvas and all items inside
    for tag in ("bg", "icon", "label"):
        canvas.tag_bind(tag, "<Enter>", on_enter)
        canvas.tag_bind(tag, "<Leave>", on_leave)
        canvas.tag_bind(tag, "<Button-1>", lambda e: command())        
        canvas.bind("<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.bind("<Leave>", lambda e: canvas.config(cursor=""))
        canvas.tag_bind(bg, "<Enter>", on_enter)
        canvas.tag_bind(icon, "<Enter>", on_enter)
        canvas.tag_bind(label, "<Enter>", on_enter)
        canvas.tag_bind(bg, "<Leave>", on_leave)
        canvas.tag_bind(icon, "<Leave>", on_leave)
        canvas.tag_bind(label, "<Leave>", on_leave)
        canvas.tag_bind(bg, "<Button-1>", on_click)
        canvas.tag_bind(icon, "<Button-1>", on_click)
        canvas.tag_bind(label, "<Button-1>", on_click)

    return canvas

#buttonsStarting-
diffopt = tk.StringVar()
btn_easy = create_canvas_button(windowstart, 100, 100, root.normalbtnimg, root.easyimg, "Easy", lambda: set_difficulty('easy'), hover_image=root.hoverbtnimg)
btn_normal = create_canvas_button(windowstart, 100, 160, root.normalbtnimg, root.normalimg, "Normal", lambda: set_difficulty('normal'), hover_image=root.hoverbtnimg)
btn_hard = create_canvas_button(windowstart, 100, 220, root.normalbtnimg, root.hardimg, "Hard", lambda: set_difficulty('hard'), hover_image=root.hoverbtnimg)
btn_impossible = create_canvas_button(windowstart, 100, 280, root.normalbtnimg, root.impossimg, "Impossible", lambda: set_difficulty('impossible'), hover_image=root.hoverbtnimg, width=160)

#GameButtons
buttonRock = ttk.Button(master=windowgame, text='Rock', command=lambda: rps_play("rock"))
buttonPaper = ttk.Button(master=windowgame, text='Paper', command=lambda: rps_play("paper"))
buttonScissors = ttk.Button(master=windowgame, text='Scissors', command=lambda: rps_play("scissors"))
result_label = ttk.Label(windowgame, text="", font=("Calibri", 14))
result_label.pack(pady=20)

buttonRock.pack()
buttonPaper.pack()
buttonScissors.pack()

windowstart.mainloop()

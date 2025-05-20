import tkinter as tk
from tkinter import messagebox, Label
from PIL import Image, ImageTk, ImageFont, ImageDraw
import ttkbootstrap as ttk
from ttkbootstrap import Style, Window
import os
import sys

from rps_logic import diff_easy, diff_normal, diff_hard, diff_impossible

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# windows
root = Window(themename='darkly')
root.withdraw()

windowstart = tk.Toplevel(root)
windowstart.title("Simple Rock, Paper, Scissors!")
windowstart.geometry('800x400')

windowgame = tk.Toplevel(root)
windowgame.withdraw()
windowgame.title("Enter your choice (rock, paper, scissors): ")
windowgame.geometry('800x400')

diffopt = tk.StringVar()

# main stuff funcs

def rps_play(player_choice):
    selected = diffopt.get()
    if selected == "easy":
        diff_easy(player_choice, windowgame, show_start_window)
    elif selected == "normal":
        diff_normal(player_choice, windowgame, show_start_window)
    elif selected == "hard":
        diff_hard(player_choice, windowgame, show_start_window)
    elif selected == "impossible":
        diff_impossible(player_choice, windowgame, show_start_window)
        
def set_difficulty(level):
    diffopt.set(level)
    windowstart.withdraw()
    setup_game_buttons()
    windowgame.deiconify()

def setup_game_buttons():
    for widget in windowgame.winfo_children():
        widget.destroy()
    ttk.Label(windowgame, text="Choose your move:", font=("Segoe UI", 14, "bold")).place(x=280, y=20)
    rock_btn = tk.Button(windowgame, image=rockimg, command=lambda: rps_play("rock"), borderwidth=0, bg="#1e1e1e", activebackground="#1e1e1e", cursor="hand2")
    rock_btn.place(x=120, y=80)
    paper_btn = tk.Button(windowgame, image=paperimg, command=lambda: rps_play("paper"), borderwidth=0, bg="#1e1e1e", activebackground="#1e1e1e", cursor="hand2")
    paper_btn.place(x=320, y=80)
    scissors_btn = tk.Button(windowgame, image=scissorsimg, command=lambda: rps_play("scissors"), borderwidth=0, bg="#1e1e1e", activebackground="#1e1e1e", cursor="hand2")
    scissors_btn.place(x=520, y=80)

def show_start_window():
    diffopt.set("")
    windowstart.deiconify()

# font and style stuff
font_path = resource_path("assets/segoeui.ttf")
bold_font = ImageFont.truetype(font_path, size=10)
style = Style()
style.configure("HoverStyle.TButton", font=("Segoe UI", 10, "bold"), borderwidth=0, padding=6, relief='flat')
style.map("HoverStyle.TButton", foreground=[("active", "white")], background=[("active", "")])

# asset paths
image_paths = {
    'easy': resource_path("assets/easy.png"),
    'normal': resource_path("assets/normal.png"),
    'hard': resource_path("assets/hard.png"),
    'impossible': resource_path("assets/impossible.png"),
    'btn_normal': resource_path("assets/btn_normal.png"),
    'btn_hover': resource_path("assets/btn_hover.png"),
}

rock = resource_path("assets/rock.png")
paper = resource_path("assets/paper.png")
scissors = resource_path("assets/scissors.png")
splash = resource_path("assets/splashimage.png")
rock_re = Image.open(resource_path("assets/rock.png")).resize((80, 80))
paper_re = Image.open(resource_path("assets/paper.png")).resize((80, 80))
scissors_re = Image.open(resource_path("assets/scissors.png")).resize((80, 80))
splash_re = Image.open(splash).resize((250, 250)).convert("RGBA")
#transparency = [splash_re, rock_re, paper_re, scissors_re]
background = Image.new("RGBA", splash_re.size, (30, 30, 30, 255))  # RGB for #1e1e1e
flattened = Image.alpha_composite(background, splash_re)
splashimg = ImageTk.PhotoImage(splash_re)
root.splashimg = splashimg
rockimg = ImageTk.PhotoImage(rock_re)
paperimg = ImageTk.PhotoImage(paper_re)
scissorsimg = ImageTk.PhotoImage(scissors_re)

images = {}
for key, path in image_paths.items():
    img = Image.open(path).resize((40, 40)) if 'btn' not in key and 'splash' not in key else Image.open(path).resize((180, 60))
    images[key] = ImageTk.PhotoImage(img)
    root.__setattr__(f"img_{key}", images[key])

# floating logo
splash_label = Label(windowstart, image=splashimg, border=0)
splash_label.place(x=500, y=80)
splash_y = 80
float_direction = 1

def float_splash():
    global splash_y, float_direction
    splash_y += float_direction
    if splash_y >= 100 or splash_y <= 70:
        float_direction *= -1
    splash_label.place(x=500, y=splash_y)
    windowstart.after(50, float_splash)

float_splash()

# difficulty button canvas
def create_canvas_button(master, x, y, bg_image, icon_image, text, command, hover_image=None):
    canvas = tk.Canvas(master, width=240, height=80, highlightthickness=0, bg="black", bd=0)
    canvas.place(x=x, y=y)
    bg = canvas.create_image(0, 0, image=bg_image, anchor="nw", tags="bg")
    icon = canvas.create_image(5, 30, image=icon_image, anchor="w")
    label = canvas.create_text(50, 30, text=text, anchor="w", font=("Segoe UI", 10, "bold"), fill="white")

    def on_enter(event):
        canvas.config(cursor="hand2")
        if hover_image:
            canvas.itemconfig(bg, image=hover_image)

    def on_leave(event):
        canvas.config(cursor="")
        canvas.itemconfig(bg, image=bg_image)

    def on_click(event):
        command()

    for tag in ("bg", "icon", "label"):
        canvas.tag_bind(tag, "<Enter>", on_enter)
        canvas.tag_bind(tag, "<Leave>", on_leave)
        canvas.tag_bind(tag, "<Button-1>", on_click)

    canvas.bind("<Enter>", on_enter)
    canvas.bind("<Leave>", on_leave)
    canvas.bind("<Button-1>", on_click)

    return canvas

# titles
ttk.Label(windowstart, text='Welcome to Simple Rock, Paper, Scissors!', font='Calibri 18 bold').pack()
ttk.Label(windowstart, text='Choose your Difficulty (Scales exponentially with each step)', font='Calibri 14').pack()

# difficulty buttons 2
create_canvas_button(windowstart, 100, 100, images['btn_normal'], images['easy'], "Easy", lambda: set_difficulty('easy'), hover_image=images['btn_hover'])
create_canvas_button(windowstart, 100, 160, images['btn_normal'], images['normal'], "Normal", lambda: set_difficulty('normal'), hover_image=images['btn_hover'])
create_canvas_button(windowstart, 100, 220, images['btn_normal'], images['hard'], "Hard", lambda: set_difficulty('hard'), hover_image=images['btn_hover'])
create_canvas_button(windowstart, 100, 280, images['btn_normal'], images['impossible'], "Impossible", lambda: set_difficulty('impossible'), hover_image=images['btn_hover'])

windowstart.mainloop()

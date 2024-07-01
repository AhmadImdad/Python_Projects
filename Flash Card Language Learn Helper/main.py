import tkinter as tk
import random
import pandas as pd
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT = "arial"
SECONDS = 3
word = {}

# --------------------------------CSV Panda File Reading-------------------------------#
try:
    data = pd.read_csv("learnt_french_words.csv")
except FileNotFoundError:
    try:
        data = pd.read_csv("french_words.csv")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning",
                               message="File not exists !")
    else:
        words_list = data.to_dict(orient="records")
else:
    words_list = data.to_dict(orient="records")


def show_english():
    global word
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")


def countdown(seconds):
    global flip_timer
    if seconds > 0:
        flip_timer = screen.after(1000, countdown, seconds - 1)
    else:
        show_english()


def tick_button_click():
    global word, flip_timer, words_list
    words_list.remove(word)
    data2 = pd.DataFrame(words_list)
    data2.to_csv("learnt_french_words.csv", index=False)
    screen.after_cancel(flip_timer)
    word = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    countdown(SECONDS)


def cross_button_click():
    global word, flip_timer
    screen.after_cancel(flip_timer)
    word = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    countdown(SECONDS)


# --------------------------------UI SETUP---------------------------------------------#
screen = tk.Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flash Card Language Learning")


card_front_image = tk.PhotoImage(file="card_front.png")
card_back_image = tk.PhotoImage(file="card_back.png")

canvas = tk.Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR,
              highlightthickness=0)
canvas_image = canvas.create_image(400, 263,
                                   image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 70, text="",
                              font=(FONT, 40, "normal"))
word_text = canvas.create_text(400, 250, text="",
                               font=(FONT, 60, "bold"))

cross_image = tk.PhotoImage(file="wrong.png")
cross_button = tk.Button()
cross_button.config(image=cross_image,
                    bg=BACKGROUND_COLOR,
                    highlightthickness=0, command=cross_button_click)
cross_button.grid(row=1, column=0)
tick_image = tk.PhotoImage(file="right.png")
tick_label = tk.Button()
tick_label.config(image=tick_image,
                  bg=BACKGROUND_COLOR,
                  highlightthickness=0, command=tick_button_click)
tick_label.grid(row=1, column=1)
flip_timer = screen.after(3000, func=show_english)
cross_button_click()
screen.mainloop()

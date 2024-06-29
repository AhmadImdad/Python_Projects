import tkinter
import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    global times_done
    global check_mark
    screen.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    times_done = 0
    check_mark = ''
    label.config(text="Timer")
    check_label.config(text=check_mark)


# ---------------------------- TIMER MECHANISM ------------------------------- #
times_done = 0
check_mark = ''


def start_button_click():
    global times_done
    work_min = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    if times_done == 0 or times_done == 2 or times_done == 4 or times_done == 6:
        label.config(text="Work")
        countdown(work_min * 60)
        times_done += 1
    elif times_done == 1 or times_done == 3 or times_done == 5:
        label.config(text="Break", fg=RED)
        countdown(short_break * 60)
        times_done += 1
    elif times_done == 7:
        label.config(text="Break", fg=RED)
        countdown(long_break * 60)
        times_done += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    global check_mark
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes <= 9:
        minutes = f"0{minutes}"
    if seconds <= 9:
        seconds = f"0{seconds}"
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = screen.after(10, countdown, count - 1)
    else:
        if times_done % 2 == 0:
            check_mark += '✔'
        check_label.config(text=check_mark)
        start_button_click()


# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Focus")
screen.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas()
canvas.config(width=230, height=230, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(115, 115, image=image)
canvas_text = canvas.create_text(115, 130,
                                 text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=1, column=1)

label = tk.Label()
label.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)
check_label = tk.Label()
check_label.config(fg=GREEN, bg=YELLOW,
                   font=(FONT_NAME, 15, "bold"), compound="bottom")
check_label.grid(row=2, column=1)

start_button = tk.Button()
start_button.config(text="Start", highlightthickness=0, command=start_button_click)
start_button.grid(row=2, column=0)
reset_button = tk.Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_click)
reset_button.grid(row=2, column=2)

screen.mainloop()

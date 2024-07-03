import tkinter
import quiz_brain

THEME_COLOR = "#375362"
FONT = "Arial"
FONT_SIZE = 15


class UI:
    def __init__(self, question):
        self.question = question
        self.score = 0
        self.screen = tkinter.Tk()
        self.screen.title("Quizzo")
        self.screen.config(padx=30, pady=30, bg=THEME_COLOR)
        self.screen.grid_rowconfigure(0, minsize=50)
        self.screen.grid_rowconfigure(0, weight=1)
        self.screen.grid_rowconfigure(2, minsize=130)
        self.screen.grid_rowconfigure(2, weight=1)
        self.score_label = tkinter.Label()
        self.score_label.config(text="Score : 0", justify='right',
                                bg=THEME_COLOR, highlightthickness=0, fg="white",
                                font=(FONT, FONT_SIZE, "normal"))
        self.score_label.grid(row=0, column=1, sticky="NE")
        self.canvas = tkinter.Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0)
        self.canvas_label = self.canvas.create_text(150, 125,
                                                    text=f"{self.question.next_question()}",
                                                    font=(FONT, FONT_SIZE, "italic")
                                                    , width=290,
                                                    justify="center", anchor="center")
        self.canvas.grid(row=1, column=0, columnspan=2)
        tick_image = tkinter.PhotoImage(file="images/true.png")
        self.tick_button = tkinter.Button()
        self.tick_button.config(image=tick_image,
                           highlightthickness=0, command=self.tick_button_clicked)
        self.tick_button.grid(row=2, column=0, sticky="S")
        cross_image = tkinter.PhotoImage(file="images/false.png")
        self.cross_button = tkinter.Button()
        self.cross_button.config(image=cross_image,
                            highlightthickness=0, command=self.cross_button_clicked)
        self.cross_button.grid(row=2, column=1, sticky="S")
        self.screen.mainloop()

    def tick_button_clicked(self):
        if self.question.question_number < 11:
            temp = self.question.check_answer("True")
            if temp > self.score:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.score = temp
            self.screen.after(1000, func=self.give_next_question)
            self.tick_button.config(state="disabled")

    def cross_button_clicked(self):
        if self.question.question_number < 11:
            temp = self.question.check_answer("False")
            if temp > self.score:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.score = temp
            self.screen.after(1000, func=self.give_next_question)
            self.cross_button.config(state="disabled")

    def give_next_question(self):
        self.tick_button.config(state="active")
        self.cross_button.config(state="active")
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score :{self.score}")
        self.canvas.itemconfig(self.canvas_label, text=self.question.next_question())


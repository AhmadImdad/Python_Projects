import tkinter as tk

choice = 0

window = tk.Tk()
window.minsize(width=300, height=200)
window.title("Miles to Km Converter")
window.config(padx=40, pady=40)


def on_click():
    global choice
    if choice == 2:
        kilometers_ = entry.get()
        if kilometers_.isdigit():  # Check if input is a valid integer
            kilometers_ = int(kilometers_)
            kilometers_ //= 1.609
            round(kilometers_, 0)
            label3.config(text=f"{kilometers_} miles.")
        else:
            label3.config(text="Please enter a valid number.")
    elif choice == 1:
        miles_ = entry.get()
        if miles_.isdigit():  # Check if input is a valid integer
            miles_ = int(miles_)
            miles_ *= 1.609
            label3.config(text=f"{miles_} kilometers.")
        else:
            label3.config(text="Please enter a valid number.")


def on_entry_click(event):
    if entry.get() == "Enter miles or Kilometers":
        entry.delete(0, tk.END)


def set_miles():
    global choice
    choice = var.get()


def set_kilometer():
    global choice
    choice = var.get()


label = tk.Label(text=" is equal to ", font=("Times new Roman", 15, "normal"))
label.grid(row=1, column=0)
# label2 = tk.Label(text="Miles", font=("Times new Roman", 15, "normal"))
# label2.grid(row=0, column=2)
label3 = tk.Label(text="0", font=("Times new Roman", 15, "normal"))
label3.grid(row=1, column=1)
# label4 = tk.Label(text="Km", font=("Times new Roman", 15, "normal"))
# label4.grid(row=1, column=2)

entry = tk.Entry(width=50)
entry.insert(tk.END, "Enter miles or Kilometers")
entry.bind('<FocusIn>', on_entry_click)
entry.grid(row=0, column=1)

button = tk.Button(text="Calculate", command=on_click)
button.grid(row=2, column=1)

var = tk.IntVar()

miles_button = tk.Radiobutton(window, text="Miles", value=1,
                              variable=var, command=set_miles,
                              font=("Times New Roman", 15, "normal"))
miles_button.grid(padx=20, row=0, column=3, sticky=tk.W)

kilometer_button = tk.Radiobutton(window, text="Kilometers", value=2,
                                  variable=var, command=set_kilometer,
                                  font=("Times New Roman", 15, "normal"))
kilometer_button.grid(padx=20, row=1, column=3, sticky=tk.W)

window.mainloop()

import time
from tkinter import *
from tkinter.font import Font
#  content -----------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SORT_BRECK_MIN = 5
LONG_BRECK_MIN = 20

#  TIMER SETTING ---------------------------------


#  TIME MACHINE ---------------------------------

def start_timer():
    count_down(5*60)

#  COUNDOWN MACHINE ---------------------------------


def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        Window.after(1000, count_down, count-1)


#  UI MACHINE ---------------------------------
Window = Tk()
Window.title("promodoro")
Window.config(padx=100, pady=50, bg=YELLOW)
count_down(5)

title_label = Label(text="Timer", fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="black")
timer_text = canvas.create_text(103, 112, text="00:00", fill="white",
                                font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN)
check_marks.grid(column=1, row=3)

Window.mainloop()

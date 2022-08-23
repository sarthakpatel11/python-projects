from os import write
from tkinter import *
from tkinter import messagebox
import random
from password_genreter import final_password

#  constant ----------
entered_password = final_password

#  function -----------------


def generat_password():
    input_password.insert(0, final_password)


def submit():
    if input_emal.get() == "" and input_password.get() == "" or input_website.get() == "":
        messagebox.showerror(
            title="Fail", message="You have to fill all the box.")
    else:
        with open("D:/Learning Stuff/python/python -Angele Yu/day_29 password genreter/pass.txt", mode="a") as txt_file:
            if input_password.get() != "":
                entered_password = input_password.get()
            else:
                entered_password = final_password
            # print(input_emal.get(), input_password.get(), entered_password)

            text = f"{input_website.get()} | {input_emal.get()} | {entered_password}\n"
            txt_file.write(text)
            messagebox.showinfo(
                title="Success", message="You have successfully save your data")
            input_website.delete(0, END)
            input_password.delete(0, END)


def search():
    pass

#  ui ------------------------------


#  windows --------
window = Tk()
window.title("My Password Genreter/Keeper")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# webstie ----------

text_label_website = Label(text="website", font=("Arial", 25, "bold"))
text_label_website.grid(column=0, row=1)

input_website = Entry()
input_website.grid(column=1, row=1)

# search ------------

# button_password_genreter = Button(
#     text="Search", command=search)
# button_password_genreter.grid(column=2, row=1)

# email ------------

text_label_emal = Label(text="emal", font=("Arial", 25, "bold"))
text_label_emal.grid(column=0, row=2)

input_emal = Entry()
input_emal.insert(0, "abc@xyz.ijk")
input_emal.grid(column=1, row=2)

# password ---------

text_label_password = Label(text="password", font=("Arial", 25, "bold"))
text_label_password.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3)

# random-password -----------

button_password_genreter = Button(
    text="click to genter password", command=generat_password)
button_password_genreter.grid(column=2, row=3)

# submit -------------

button_submit = Button(text="click me", command=submit)
button_submit.grid(column=1, row=4)


window.mainloop()

import tkinter


# window----------------
window = tkinter.Tk()
window.title("My First Time.")
window.minsize(width=500, height=300)

# lebale ---------------

my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()

#  button ----------------


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click To Convert", command=button_clicked)
button.pack()

# input --------------

input = tkinter.Entry(width=10)
input.pack()
print(input.get())

window.mainloop()


# kwarg ---------------------------------------------------

# def add(*arg):
#     sum = 0
#     for i in arg:
#         sum += i
#     return sum


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def calc(**kwarg):
#     for key, value in kwarg.items():
#         print(key)
#         print(value)


# calc(add=3, multiply=5)


# class car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")


# new_car = car(make="nissan", model="GT-R")
# print(new_car.make)
# print(new_car.model)
# print(new_car.color)


# #  chellange --------------------------------------------------


# # window----------------
# window = tkinter.Tk()
# window.title("My First Time.")
# window.minsize(width=500, height=300)

# # input --------------

# input = tkinter.Entry(width=20)
# input.pack()
# print(input.get())

# #  button ----------------


# def button_clicked():
#     miles = float(input.get())
#     ans = round(miles*1.609, 2)
#     my_label_ans = tkinter.Label(text=ans, font=("Arial", 24))
#     my_label_ans.pack()


# button = tkinter.Button(text="Click To Convert", command=button_clicked)
# button.pack()
# # button.place(x=350, y=0)

# # lebale ---------------

# my_label_qna = tkinter.Label(
#     text="miles", font=("Arial", 24))
# my_label_qna.pack()
# my_label_qna.place(x=300, y=-10)

# my_label_kilo = tkinter.Label(
#     text="kilo", font=("Arial", 24))
# my_label_kilo.pack()
# my_label_kilo.place(x=300, y=45)
# window.mainloop()

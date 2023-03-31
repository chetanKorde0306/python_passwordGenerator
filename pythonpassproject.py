
# from secrets import choice
from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_character = string.punctuation
    all = small_alphabets+capital_alphabets+numbers+special_character
    password_length = int(length_Box.get())

#    password = random.sample(all,password_length)
#    passwordFeild.insert(0,password)
    if choice.get() == 1:
            passwordFeild.insert(0, random.sample(small_alphabets, password_length))

    if choice.get() == 2:
            passwordFeild.insert(0, random.sample(small_alphabets+capital_alphabets, password_length))

    if choice.get() == 3:
            passwordFeild.insert(0, random.sample(all, password_length))

def copy():
    random_password=passwordFeild.get()
    pyperclip.copy(random_password)
root = Tk()
root.config(bg='orange')
choice = IntVar()
Font = ('arial', 13, 'bold')
# 3b9e9f
# header
passwordLabel = Label(root, text='Password Generator', font=('times_new_roman',20,'bold'),bg = "orange",fg='white')
passwordLabel.grid(pady=10)


weakradioButton = Radiobutton(root, text = "Weak", value=1, variable=choice, font=Font )
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text = "Medium", value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text = "Strong", value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)


lengthLabel = Label(root, text='Password length', font=(Font,20,'bold'),bg = "orange",fg='white')
lengthLabel.grid()

length_Box = Spinbox(root, from_=5 , to_=25, width=5,font=Font)
length_Box.grid()

genrateButton = Button(root, text = "Generate", font = Font, command = generator)
genrateButton.grid(pady=5)

passwordFeild = Entry(root, width=25, bd=2, font= Font)
passwordFeild.grid()

copyButton = Button(root, text= "Copy Password", font = Font,command = copy)
copyButton.grid(pady=5)

root.mainloop()

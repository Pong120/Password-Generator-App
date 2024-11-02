import random
import string
from tkinter import *
from tkinter import messagebox


def generator_password():
    try:
        length = int(length_entry.get())
        repeat = int(repeat_entry.get())

        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        punctuation = string.punctuation
        digit = string.digits

        characters = upper + lower + punctuation + digit

        if repeat == '1':
            password = random.sample(characters, length)
        else:
            password = [
                random.choice(upper),
                random.choice(lower),
                random.choice(punctuation),
                random.choice(digit)
            ]

            password += random.choices(characters, k=length-4)

        random.shuffle(password)
        str_password = ''.join(password)
        result_text.set(f'Your password is {str_password}!!!')
    except:
        messagebox.showerror('Error', 'Please enter valid number!!')


gen_app = Tk()
gen_app.geometry('350x200')
gen_app.title('Python')

title_label = Label(gen_app, text="Password Generator App", font=('Ubuntu Mono', 12))
title_label.pack()

length_label = Label(gen_app, text="length of password: ")
length_label.place(x=20, y=30)
length_entry = Entry(gen_app, width=3)
length_entry.place(x=190, y=30)

repeat_label = Label(gen_app, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20, y=60)
repeat_entry = Entry(gen_app, width=3)
repeat_entry.place(x=300, y=60)

password_button = Button(gen_app, text="Generate", command=generator_password)
password_button.place(x=100, y=100)

result_text = StringVar()
result_label = Label(gen_app, textvariable=result_text, font=("Helvetica", 12))
result_label.place(x=60, y=120)

gen_app.mainloop()


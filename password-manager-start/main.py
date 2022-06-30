from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pas_generator():
    pas.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_sym + password_num

    shuffle(password_list)
    password = ''.join(password_list)
    pas.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_web = web.get()
    new_mail = mail.get()
    new_pas = pas.get()
    new_dict = {
        new_web: {
            "email": new_mail,
            "password": new_pas
        }
    }

    if new_web == "" or new_pas == "":
        messagebox.showinfo(title="Oops",
                            message="Looks like you left the box empty. Please type something on that blank box they are starving for your response.")
    else:
        try:
            with open("Data.jason", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("Data.jason", "w") as file:
                json.dump(new_dict, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_dict)
            with open("Data.jason", "w") as file:
                # Saving new data
                json.dump(data, file, indent=4)
        finally:
            web.delete(0, END)
            pas.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = web.get()
    try:
        with open("Data.jason", "r") as file:
            data = json.load(file)
        if website in data:
            messagebox.showinfo(title=f"{website}",
                                message=f"email: {data[website]['email']}\n password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data files are found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

l1 = Label(text="Website:")
l1.grid(column=0, row=1)

web = Entry(width=21)
web.focus()
web.grid(column=1, row=1)

l2 = Label(text="Email/Username:")
l2.grid(column=0, row=2)
mail = Entry(width=35)
mail.grid(column=1, row=2, columnspan=2)
mail.insert(0, "password@email.com")

l3 = Label(text="Password:")
l3.grid(column=0, row=3)
pas = Entry(width=21)
pas.grid(column=1, row=3)

b1 = Button(text="Generate password", command=pas_generator)
b1.grid(column=2, row=3)
b2 = Button(text="Add", width=36, command=save_password)
b2.grid(column=1, row=4, columnspan=2)
b3 = Button(text="Search", command=find_password, width=13)
b3.grid(column=2, row=1)

window.mainloop()

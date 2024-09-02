from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json



# Search
def search():
    website = entry_1.get()

    try:
        with open("data.json", mode = "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            pass__word = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email : {email} \n Password : {pass__word}")

        else:
            messagebox.showinfo(title = "Error", message = f"No details of {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for char in range(randint(8, 10)) ]

    symbol_list = [choice(symbols) for i in range(randint(2, 4)) ]

    numbers_list = [choice(numbers) for n in range(randint(2, 4))]

    password_list = letters_list + symbol_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    entry_3.insert(0, f"{password}")

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #)

def save_password():
    website = entry_1.get()
    email = entry_2.get()
    pass_word = entry_3.get()

    new_data = {
        website : {
            "email" : email,
            "password" : pass_word
        }
    }

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title= "Error",
                               message=f"Please don't leave any fields empty")

    else:
        try:
            with open("data.json", mode = "r") as file:
                # load the data
                data = json.load(file)

        except FileNotFoundError:
                with open ("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

        else:
            # Update the data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Write the new data
                json.dump(data, file, indent=4)

        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canva = Canvas(width = 200, height=200)
password = PhotoImage(file = "logo.png")
canva.create_image(100, 100, image = password)
canva.grid( column = 1, row = 0)

label_1 = Label(text = "Website: ")
label_1.grid(column = 0, row = 1)

entry_1 = Entry(width = 23, border= 0)
entry_1.grid(column = 1, row = 1)

label_2 = Label(text = "Email/Username: ")
label_2.grid(column = 0, row = 2)

entry_2 = Entry(width = 40, border= 0)
entry_2.grid(column = 1, row = 2, columnspan = 2)
entry_2.insert(0, "njorogeofrey7@gmail.com")

label_3 = Label(text = "Password: ")
label_3.grid(column = 0, row = 3)

entry_3 = Entry(width = 23, border= 0)
entry_3.grid(column = 1, row = 3)

button0 = Bi=Button(text = " Search",border= 0, highlightthickness=0, command= search)
button0.grid(column = 2, row =1)

button1 = Button(text = "Generate Password",border= 0, highlightthickness=0, command= generate)
button1.grid(column = 2, row =3)

button2 = Button(text = "Add", width= 34, border=0.5, highlightthickness=0, command= save_password)
button2.grid(column = 1, row =4, columnspan = 2)
window.mainloop()
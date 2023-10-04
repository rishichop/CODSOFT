from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%',
           '&', '(', ')', '*', '+']


def generate_password():
    length = int(length_entry.get())
    password_entry.delete(0, END)
    password_list = []

    for i in range(length):
        password_list.append(choice(letters))

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


def save():
    website = website_entry.get().title()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.", )

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            if website in data:
                messagebox.showinfo(title="Oops", message="This Website is already in the password list.")
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    key = website_entry.get().title()
    if key == "":
        messagebox.showinfo(title="Oops", message="Please fill in the Website Entry.")
        return
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")

    else:
        if key in data:
            messagebox.showinfo(title="Website Found!", message=f"website: {key}"
                                                                f"\nemail: {data[key]['email']}"
                                                                f"\npassword: {data[key]['password']}.")
        else:
            messagebox.showinfo(title="Website not Found!", message="This website is not added in password list.")
    finally:
        website_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

Website_label = Label(text="Website:")
Website_label.grid(column=0, row=0)

length_label = Label(text="Length:")
length_label.grid(column=0, row=1)

Email_Username_label = Label(text="Email/Username:")
Email_Username_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

website_entry = Entry(width=21, borderwidth=3)
website_entry.grid(column=1, row=0, sticky="EW")
website_entry.focus()

length_entry = Entry(width=21, borderwidth=3)
length_entry.insert(0, "10")
length_entry.grid(column=1, row=1, sticky="EW")

email_username_entry = Entry(width=21, borderwidth=3)
email_username_entry.insert(0, "Something@gmail.com")
email_username_entry.grid(column=1, row=2, sticky="EW")

password_entry = Entry(width=21, borderwidth=3)
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password", width=14, command=generate_password, borderwidth=3)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save, borderwidth=3)
add_button.grid(column=1, row=5, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=14, command=search, borderwidth=3)
search_button.grid(column=2, row=0)

window.mainloop()

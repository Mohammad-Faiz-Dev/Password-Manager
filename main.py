from tkinter import *
from tkinter import messagebox
from random import randint,choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE INPUT ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please don't leave any empty fields")
        return

    messagebox_ok = messagebox.askokcancel(title="Confirmation",
                                         message=f"Website: {website}\nEmail/Username: {email}\nPassword: {password}\nSave data?")

    if not messagebox_ok:
        messagebox.showinfo(title="Data not saved", message="The data was not saved.")
        return

    try:
        with open("data.json", "r") as data_file:
            # Try to read existing data
            try:
                data = json.load(data_file)
            except json.decoder.JSONDecodeError:
                # If file is empty or invalid, start with empty dict
                data = {}
    except FileNotFoundError:
        # If file doesn't exist, create it with new data
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        # Update existing data and save
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_username_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="Input Error", message="Please enter a website to search for.")
        return
    try:
        with open("data.json", "r") as json_data:
            data = json.load(json_data)
            if website in data: #searches for website in json file
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Not Found", message=f"No details found for '{website}'")
    except FileNotFoundError:
        messagebox.showinfo(title="Alert", message="No Data Found")
# ---------------------------- SEARCH SAVED PASSWORD ------------------------------- #
window = Tk()
window.title("MyPass")
window.minsize(width=300, height=300)
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=189)
canvas.grid(column=1, row=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo_img)

#adding the Label #1
website_label = Label(text="Website:",font=("Arial", 10,))
website_label.grid(column=0, row=1)

#label #2
email_username_label = Label(text="Email/Username:",font=("Arial", 10,))
email_username_label.grid(column=0, row=2)

#label #3
password_label = Label(text="Password:",font=("Arial", 10,))
password_label.grid(column=0, row=3)

#adding entry-box #1
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

#adding entry-box #2
email_username_entry = Entry(width=48)
email_username_entry.grid(column=1, row=2, columnspan=3)


#adding entry-box #3
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

#adding the button #1
generate_button = Button(text="Generate", width=11, command=generate_password)
generate_button.grid(column=3, row=3)

#adding the button #2
add_button = Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=3)

#adding the button #3
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=3,row=1)














window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters  + password_numbers + password_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data={
        website : {
            "email": username,
            "password": password
        }
    }

    if (len(website)==0) or (len(password) ==0):
        messagebox.showwarning(title="Oops!!!",message="Please don't leave any fields empty!")
    else:
    #     is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {username} \nPasswrd: {password} \nIs it ok to save?")
    # # messagebox.showinfo(title="Title",message="message")
    #     if is_ok:

            # file.write(f"{website} | {username} | {password}\n")
        try:
            with open("Data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("Data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website=website_input.get()
    try:
        with open("Data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password= data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

username_label=Label(text="Email/Username:")
username_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

# entry
website_input=Entry(width=26)
website_input.grid(row=1,column=1)
website_input.focus()



username_input=Entry(width=45)
username_input.grid(row=2,column=1,columnspan=2)
username_input.insert(0, "purviharpalani.24@gmail.com")


password_input=Entry(width=26)
password_input.grid(row=3,column=1)


# buttons
search_button=Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)

generate_password=Button(text="Generate Password",width=15,command=generate_password)
generate_password.grid(row=3,column=2)

add_button=Button(text="Add",width=38,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
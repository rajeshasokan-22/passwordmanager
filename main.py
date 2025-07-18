from tkinter import *
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webs = website_entry.get()
    usr = username_entry.get()
    pas = password_entry.get()
    new_data = {
        webs: {
            "email": usr,
            "password": pas,
        }
    }
    if len(webs) == 0 or len(pas) == 0 or len(usr) == 0:
        messagebox.showwarning(title="Oops",message="Don't leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=webs,message=f"Website: {webs}\nUsername: {usr}\nPassword: {pas}\nClick Ok to Save!")
        if is_ok:
            try:
                with open("password.json","r") as json_file:
                    data = json.load(json_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password.json","w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                with open("password.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                    print("data_added")
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------------------- SEARCH -------------------------------- #
def find_password():
    web = website_entry.get()
    try:
        with open("password.json","r") as json_file:
            dict = json.load(json_file)
            flag = 0
            for key in dict:
                if key.lower() == web.lower():
                    mssg = ""
                    for inner_key in dict[key]:
                        mssg += f"{inner_key}: {dict[key][inner_key]}\n"
                    messagebox.showinfo(key,message=mssg)
                    print(mssg)
                    flag = 1
            if flag == 0:
                messagebox.showerror(title="Error",message=f"{web} Data not found")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="JSON file not found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2,column=1)
username_entry.insert(0,"rajesh.asokan@edveon.com")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

website = Label(text="Website:",bg="white")
website.grid(row=1,column=0)
username = Label(text="Email/Username:",bg="white")
username.grid(row=2,column=0)
password = Label(text="Password:",bg="white")
password.grid(row=3,column=0)

gp_button = Button(text="Generate Password",command=generate_password,bg="white")
gp_button.grid(row=3,column=2,padx=10)

add_button = Button(text="Add",width=30,bg="white",command=save)
add_button.grid(row=4,column=1)

search_button = Button(text="Search",width=14,command=find_password,bg="white")
search_button.grid(row=1,column=2,padx=10)
window.mainloop()
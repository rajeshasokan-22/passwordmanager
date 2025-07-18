from tkinter import *
import random
from tkinter import messagebox
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
    is_ok = None
    if len(webs) == 0 or len(pas) == 0 or len(usr) == 0:
        messagebox.showwarning(title="Oops",message="Don't leave the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=webs,message=f"Website: {webs}\nUsername: {usr}\nPassword: {pas}\nClick Ok to Save!")
    if is_ok:
        with open("password.txt","a") as pf:
            pf.write(f"{webs} | {usr} | {pas}\n")
        website_entry.delete(0,END)
        username_entry.delete(0,END)
        password_entry.delete(0,END)

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
window.mainloop()
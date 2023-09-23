from tkinter import *
import json
from tkinter import messagebox
from Home import Home_page


class signup:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x1000")
        self.insta_image = PhotoImage(file='insta.png')
        for widget in self.root.winfo_children():
            widget.destroy()


        ############### Frame ##############
        self.frame_user_info = Frame(self.root, bg="white", width=300, height=680)
        self.frame_user_info.place(x=550, y=10)

        self.txt = 'SIGN UP'
        self.label_welcome = Label(self.frame_user_info, text=self.txt, bg="white", fg='orange',
                                   font=("arial", 20, "bold"))
        self.label_welcome.place(x=80, y=45)

        ############# Name #############
        self.name_label = Label(self.frame_user_info, text="Name:", fg="black", bg="white",
                                font=('yu gothic wi', 13, "bold"))
        self.name_label.place(x=60, y=100)
        self.name_entry = Entry(self.frame_user_info, width=25, border=0, highlightthickness=0, relief=FLAT,
                                fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.name_entry.place(x=60, y=125)
        self.name_line = Canvas(self.frame_user_info, width=180, height=2.0, bg='black', highlightthickness=0)
        self.name_line.place(x=60, y=150)

        ############# Phone #############
        self.phone_label = Label(self.frame_user_info, text="Phone:", fg="black", bg="white",
                                 font=('yu gothic wi', 13, "bold"))
        self.phone_label.place(x=60, y=200)
        self.phone_entry = Entry(self.frame_user_info, width=25, border=0, highlightthickness=0, relief=FLAT,
                                 fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.phone_entry.place(x=60, y=225)
        self.phone_line = Canvas(self.frame_user_info, width=180, height=2.0, bg='black', highlightthickness=0)
        self.phone_line.place(x=60, y=250)

        ############# Email #############
        self.email_label = Label(self.frame_user_info, text="Email:", fg="black", bg="white",
                                 font=('yu gothic wi', 13, "bold"))
        self.email_label.place(x=60, y=300)
        self.email_entry = Entry(self.frame_user_info, width=25, border=0, highlightthickness=0, relief=FLAT,
                                 fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.email_entry.place(x=60, y=325)
        self.email_line = Canvas(self.frame_user_info, width=180, height=2.0, bg='black', highlightthickness=0)
        self.email_line.place(x=60, y=350)

        ############# Password #############
        self.password_label = Label(self.frame_user_info, text="Password:", fg="black", bg="white",
                                    font=('yu gothic wi', 13, "bold"))
        self.password_label.place(x=60, y=400)
        self.password_entry = Entry(self.frame_user_info, width=25, border=0, highlightthickness=0, relief=FLAT,
                                    fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.password_entry.place(x=60, y=425)
        self.password_line = Canvas(self.frame_user_info, width=180, height=2.0, bg='black', highlightthickness=0)
        self.password_line.place(x=60, y=450)

        ############# Submit button #############
        self.submit_button = Button(self.frame_user_info, text="Submit", width=20, cursor='hand2', bg="Orange",
                                    fg="black", font=('yu gothic wi', 13, "bold"), activebackground='white',
                                    command=self.user_data)
        self.submit_button.place(x=50, y=500)
        ############## insta image###########

        self.label_frame = Frame(self.frame_user_info, bg="white", width=20, height=30, relief="flat")
        self.label_frame.place(y=0)
        self.name_label = Label(self.label_frame, image=self.insta_image, bg="white")
        self.name_label.pack()

    def user_data(self):
        with open("user_data.json", "r") as file:
            data = json.load(file)

        email = self.email_entry.get()

        for item in data:
            if item["Email"] == email:
                messagebox.showerror("Registration Failed", "This email already exists!")
                return

        user_name = self.name_entry.get()

        for Item in data:
            if Item["User name"] == user_name:
                messagebox.showerror("Registration Failed", "This user name already exists!")
                return

        user_data = {
            "Name": self.name_entry.get(),
            "User name": self.name_entry.get(),
            "Email": self.email_entry.get(),
            "Password": self.password_entry.get()
        }

        data.append(user_data)

        with open("user_data.json", "w") as file:
            json.dump(data, file, indent=2)

        messagebox.showinfo("registration "," done successfully")
        Home_page(self.root)


class loginForm():
    def __init__(self, root):

        self.root = root
        self.root.geometry("1600x1000")
        self.insta_image = PhotoImage(file='insta.png')
        for widget in self.root.winfo_children():
            widget.destroy()

        ############## login frame ##############
        self.frame_welcome = Frame(self.root, bg="white", width=300, height=680)
        self.frame_welcome.place(x=550, y=10)

        ############# Welcome ##############
        self.txt = 'WELCOME TO INSTAGRAM !'
        self.label_welcome = Label(self.frame_welcome, text=self.txt, bg="white", fg='black',
                                   font=("arial", 15, "bold"))
        self.label_welcome.place(x=15, y=90)

        ############## Sign in #############
        self.txt2 = 'Sign in'
        self.signin_label = Label(self.frame_welcome, text=self.txt2, bg='white', fg='DarkOrange',
                                  font=('yu gothic wi', 17, "bold"))
        self.signin_label.place(x=100, y=160)

        ############ Email ###########
        self.email_label = Label(self.frame_welcome, text="Email:", fg="black", bg="white",
                                 font=('yu gothic wi', 13, "bold"))
        self.email_label.place(x=60, y=255)
        self.email_entry = Entry(self.frame_welcome, width=25, border=0, highlightthickness=0, relief=FLAT,
                                 fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.email_entry.place(x=60, y=280)
        self.email_line = Canvas(self.frame_welcome, width=180, height=2.0, bg='black', highlightthickness=0)
        self.email_line.place(x=60, y=305)

        ############# Password ###############
        self.password_label = Label(self.frame_welcome, text="Password:", fg="black", bg="white",
                                    font=('yu gothic wi', 13, "bold"))
        self.password_label.place(x=60, y=355)

        self.password_entry = Entry(self.frame_welcome, width=25, border=0, highlightthickness=0, relief=FLAT,
                                    fg='black', bg='white', font=('yu gothic wi', 11, "bold"))
        self.password_entry.place(x=60, y=380)
        self.password_line = Canvas(self.frame_welcome, width=180, height=2.0, bg='black', highlightthickness=0)
        self.password_line.place(x=60, y=405)

        ############################## Login Button ##############
        self.login = Button(self.frame_welcome, text="Login", width=20, cursor='hand2', bg="orange", fg="black",
                            font=('yu gothic wi', 13, "bold"), activebackground='white',
                            command=self.login_clicked)
        self.login.place(x=45, y=455)

        ################### Sign up####################
        self.new_account = Label(self.frame_welcome, text="Don't have an account?", fg="black", bg="white",
                                 font=('yu gothic wi', 13, "bold"))
        self.new_account.place(x=20, y=540)
        self.signup = Button(self.frame_welcome, text="Sign up", width=8, cursor='hand2', fg="DarkOrange", bg="white",
                             font=('yu gothic wi', 13, "bold"), activebackground='white', bd=0,
                             command=self.signup_clicked)
        self.signup.place(x=210, y=538)
        ############## insta image###########

        self.label_frame = Frame(self.frame_welcome, bg="white", width=20, height=30, relief="flat")
        self.label_frame.place(y=0)
        self.name_label = Label(self.label_frame, image=self.insta_image, bg="white")
        self.name_label.pack()

    def login_clicked(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        with open("user_data.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item["Email"] == email and item["Password"] == password:
                messagebox.showinfo("Login Successful", "Welcome !")

                Home_page(self.root)

                return

        messagebox.showerror("Login Failed", "Invalid email or password!")
    def signup_clicked(self):
        signup(self.root)


root = Tk()
login = loginForm(root)
root.mainloop()

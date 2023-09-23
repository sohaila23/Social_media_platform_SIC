import tkinter as tk
from tkinter import *
from s import profile_page


class others():
    def __init__(self,root):
        self.root = Tk()
        self.root = root
        self.root.geometry("1500x850")
        self.root.title("insta")
        self.face_image = PhotoImage(file='face.png')
        self.home_image = PhotoImage(file='home page.png')
        self.personal_image = PhotoImage(file='personal.png')
        self.add_image = PhotoImage(file='add.png')
        self.setting_image = PhotoImage(file='setting.png')
        self.insta_image = PhotoImage(file='insta.png')
        self.search_image = PhotoImage(file='search.png')
        self.x = 0
        self.y = 0
        self.others_frame = Frame(self.root, bg="white", width=300, height=680, relief="raised")
        self.others_frame.place(x=550, y=10)

        self.futures_frame = Frame(self.others_frame, bg="white", width=300, height=25, relief="flat")
        self.futures_frame.columnconfigure(self.x, weight=1)
        self.futures_frame.place(y=635)
        self.label_frame = Frame(self.others_frame, bg="white", width=300, height=30, relief="flat")
        self.label_frame.place(y=0)
        self.name_label = Label(self.label_frame, image=self.insta_image, bg="white")
        self.name_label.pack()
        self.user_frame = Frame(self.others_frame, bg="white", width=300, height=40)
        self.user_frame.columnconfigure(self.x, weight=1)
        self.user_frame.place(y=65)
        self.stats_frame = Frame(self.others_frame, bg="white")
        self.stats_frame.columnconfigure(self.x, weight=1)
        self.stats_frame.place(x=80, y=80)
        self.posts_label = Label(self.stats_frame, text="Posts\n10", font=("Helvetica", 10), bg="white")
        self.posts_label.pack(side=tk.LEFT, padx=10)
        self.followers_label = Label(self.stats_frame, text="Followers\n100", font=("Helvetica", 10), bg="white")
        self.followers_label.pack(side=tk.LEFT, padx=10)
        self.following_label = Label(self.stats_frame, text="Following\n200", font=("Helvetica", 10), bg="white")
        self.following_label.pack(side=tk.LEFT, padx=10)
        self.follow_button = Button(self.others_frame, relief=FLAT, text="Follow", font=("Helvetica", 10,"bold")
                                    , width=35,bg="Blue",fg="white")
        self.follow_button.place(x=5, y=200)
        self.share_frame = Frame(self.others_frame, bg="white")
        self.share_frame.place(x=30, y=300)
        self.share_label = Label(self.share_frame, text="This Account is Private", font=("Helvetica", 10,"bold"),
                                 width=30, bg="white")
        self.share_label.pack()
        self.ph_label = Label(self.share_frame, text="Follow this account to see their photos\nand videos",
                              font=("Helvetica", 10), width=30, bg="white")

        self.ph_label.pack()

        self.btn_user()
        self.futures()
        self.root.mainloop()

    def futures(self):
        settings_page = Button(self.futures_frame, image=self.setting_image, borderwidth=0, bg="white")
        settings_page.grid(row=0, column=2, padx=25)

        add_page = Button(self.futures_frame, image=self.add_image, borderwidth=0, bg="white")
        add_page.grid(row=0, column=3, padx=10)

        personal_page = Button(self.futures_frame, image=self.personal_image, borderwidth=0, bg="white")
        personal_page.grid(row=0, column=0, padx=10)

        home_page = Button(self.futures_frame, image=self.home_image, borderwidth=0, bg="white")
        home_page.grid(row=0, column=1, padx=25)

    def btn_user(self):
        self.x += 1
        button_image = Button(self.user_frame, image=self.face_image, borderwidth=0, text="sohaila esam",
                              font=("Arial", 10), compound=tk.TOP, bg="white")
        button_image.grid(row=0, column=self.x, padx=5)


#others()

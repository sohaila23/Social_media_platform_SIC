import tkinter
from tkinter import *
#from s import profile_page
from queue1 import Queue
#from others import others
from stack import Stack


class Home_page:

    def __init__(self,root):
        #self.root = Tk()
        self.root = root
        self.root.geometry("1500x850")
        for widget in self.root.winfo_children():
            widget.destroy()

        ################ photos ################

        self.root.title("insta")
        self.face_image = PhotoImage(file='face.png')
        self.home_image = PhotoImage(file='home page.png')
        self.personal_image = PhotoImage(file='personal.png')
        self.add_image = PhotoImage(file='add.png')
        self.setting_image = PhotoImage(file='setting.png')
        self.insta_image = PhotoImage(file='insta1.png')
        self.search_image = PhotoImage(file='search.png')
        self.like_before = PhotoImage(file="like before.png")
        self.Comment = PhotoImage(file="Comment.png")
        self.like_after = PhotoImage(file="like aftar.png")
        self.send_image = PhotoImage(file='send.png')
        self.send_image1 = PhotoImage(file='send1.png')

        ## varibels ##

        self.x = 0
        self.y = 0
        self.a = 0

        ##### freams ####

        self.main_frame = Frame(self.root, bg="white", width=300, height=680)
        self.main_frame.place(x=450, y=10)

        self.label_frame = Frame(self.main_frame, bg="white", width=300, height=30, relief="flat")
        self.label_frame.place(y=0)
        self.name_label = Label(self.label_frame, image=self.insta_image, bg="white")
        self.name_label.pack()

        self.search_frame = Frame(self.main_frame, bg="white", width=300, height=25)
        self.search_frame.columnconfigure(self.x, weight=1)
        self.search_frame.place(y=35)
        self.search()

        self.user_frame = Frame(self.main_frame, bg="white", width=300, height=50)
        self.user_frame.columnconfigure(self.x, weight=1)
        self.user_frame.place(x=25, y=60)
        self.btn_user()
        self.btn_user()
        self.btn_user()

        self.posts_frame = Frame(self.main_frame, bg="blue", width=300, height=480)
        self.posts_frame.columnconfigure(self.y, weight=1)
        self.posts_frame.place(y=155)

        self.posts()

        self.futures_frame = Frame(self.main_frame, bg="white", width=300, height=25, relief="flat")
        self.futures_frame.columnconfigure(self.x, weight=1)
        self.futures_frame.place(y=635)

        self.futures()

        self.root.mainloop()

        ## functions ##

    def btn_user(self):
        self.x += 1
        self.profile_frame = Frame(self.user_frame, bg="white", width=100, height=85, relief="flat")
        self.profile_frame.grid(row=0, column=self.x, padx=5)

        button_image = Button(self.profile_frame, image=self.face_image, width=100, height=60, borderwidth=0,
                              text="mohamed", font=("Arial", 7),
                              compound=tkinter.TOP, bg="white",command=self.go_other)
        button_image.place(y=0)

        button_follow = Button(self.profile_frame, text="Follow +", width=10, borderwidth=0,
                               font=('yu gothic wi', 10, "bold"),
                               fg="white", bg="Blue", command=lambda: self.follow(button_follow))
        button_follow.place(x=10, y=65)
    def go_other(self):
        others(self.root)
    def follow(self, button_follow):
        button_follow = Button(self.profile_frame, text="Friend", bg="Blue", fg="white", width=10,
                               borderwidth=0, command=lambda: self.un_follow(button_follow))
        button_follow.place(x=10, y=65)

    def un_follow(self, button_follow):
        button_follow = Button(self.profile_frame, text="Follow +", bg="Blue", fg="white", width=10,
                               borderwidth=0, command=lambda: self.follow(button_follow))
        button_follow.place(x=10, y=65)

    def search(self):
        search_entry = Entry(self.search_frame, width=30, fg='black', bg='white', font=("arial", 10))
        search_label = Label(self.search_frame, text="Search:", fg="black", bg="white")
        search_button = Button(self.search_frame, image=self.search_image, bg="white", width=20, height=15)
        search_button.place(x=260)
        search_label.place(x=0)
        search_entry.place(x=45)

    def posts(self):
        self.post = Frame(self.posts_frame, bg="white", width=280, height=480, relief="flat")
        self.post.place(x=0, y=0)

        self.data_frame = Frame(self.post, bg="white", width=260, height=40, relief="flat")
        self.data_frame.place(x=10, y=0)
        face_page = Button(self.data_frame, image=self.personal_image, text=self.x, borderwidth=0, bg="white",
                           compound=tkinter.LEFT)
        face_page.place(x=0, y=0)

        self.post_area = Frame(self.post, bg="black", width=260, height=330, relief="flat")
        self.post_area.place(x=10, y=40)

        self.interaction_area = Frame(self.post, bg="white", width=260, height=40, relief="flat")
        self.interaction_area.place(x=10, y=370)

        self.comment_frame = Frame(self.post, bg="white", width=260, height=23, relief="flat")
        self.comment_frame.place(x=10, y=410)

        Comment_button = Button(self.interaction_area, image=self.Comment, bg="white", width=130, height=30,
                                borderwidth=0, command=self.comment_click)
        Comment_button.place(x=130, y=3)

        like_button_b = Button(self.interaction_area, image=self.like_before, text=self.a, bg="white", width=130,
                               height=30, borderwidth=0, compound=tkinter.LEFT,
                               command=lambda: self.like(like_button_b))
        like_button_b.place(x=0, y=3)

    #def comment(self):
        #comment_entry = Entry(self.comment_frame, width=31, fg='black', bg='white', font=("arial", 10))
        #comment_entry.place(x=0)
        #comment_button = Button(self.comment_frame, image=self.send_image, bg="white", width=30, height=15,)
        #comment_button.place(x=222)

    def like(self, like_button_b):
        self.a += 1
        like_button_b = Button(self.interaction_area, image=self.like_after, text=self.a, bg="white", width=130,
                               height=30, borderwidth=0, compound=tkinter.LEFT,
                               command=lambda: self.like_b(like_button_b))
        like_button_b.place(x=0, y=3)

    def like_b(self, like_button_b):
        self.a -= 1
        like_button_b = Button(self.interaction_area, image=self.like_before, text=self.a, bg="white", width=130,
                               height=30, borderwidth=0, compound=tkinter.LEFT,
                               command=lambda: self.like(like_button_b))
        like_button_b.place(x=0, y=3)

    def futures(self):
        settings_page = Button(self.futures_frame, image=self.setting_image, borderwidth=0, bg="white")
        settings_page.grid(row=0, column=0, padx=15)

        send_page = Button(self.futures_frame, image=self.send_image1, borderwidth=0, bg="white"
                           ,command=self.chat_click)
        send_page.grid(row=0, column=1, padx=10)

        add_page = Button(self.futures_frame, image=self.add_image, borderwidth=0, bg="white")
        add_page.grid(row=0, column=2, padx=15)

        personal_page = Button(self.futures_frame, image=self.personal_image, borderwidth=0, bg="white"
                               , command=self.personal_clicked)
        personal_page.grid(row=0, column=3, padx=10)

        home_page = Button(self.futures_frame, image=self.home_image, borderwidth=0, bg="white")
        home_page.grid(row=0, column=4, padx=15)
    def chat_click(self):
        Chat(self.root)
    def comment_click(self):
        Comment(self.root)
    def personal_clicked(self):
        profile_page(self.root)
#Home_page()
class Comment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x680")
        self.root.configure(bg="white")
        for widget in self.root.winfo_children():
            widget.destroy()

        self.queue = Queue()

        self.frame = Frame(self.root, bg="white")
        self.frame.pack(pady=10)

        self.display_frame = Frame(self.frame, bg="white")
        self.display_frame.pack()

        self.input_frame = Frame(self.frame, bg="white")
        self.input_frame.pack(side=BOTTOM)

        self.post_entry = Text(self.input_frame, width=30, height=5)
        self.post_entry.pack(side=LEFT, pady=5)

        self.button_frame = Frame(self.input_frame, bg="white")
        self.button_frame.pack(side=LEFT, padx=5)

        self.post_button = Button(self.button_frame, text="Send", command=self.comment, bg="black", fg="white")
        self.post_button.pack(pady=5)

        self.delete_button = Button(self.button_frame, text="Delete", command=self.delete_comment, bg="black", fg="white")
        self.delete_button.pack(pady=5)

        self.back_button = Button(self.button_frame, text="back", command=self.back_click, bg="black",
                                    fg="white")
        self.back_button.pack(pady=5)
    def comment(self):
        new_message = self.post_entry.get("1.0", END).strip()
        if new_message:
            self.queue.enqueue(new_message)
            self.post_entry.delete("1.0", END)
            self.display_messages()

    def delete_comment(self):
        message = self.queue.dequeue()
        if message:
            self.display_messages()
    def back_click(self):
         Home_page(self.root)
    def display_messages(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        all_messages = self.queue.peek()
        if all_messages is not None:
            for message in all_messages:
                message_label = Label(self.display_frame, text=message, wraplength=300, bg="white")
                message_label.pack(pady=5)

class profile_page():
    def __init__(self,root):

        #self.root = Tk()
        self.root = root
        self.root.geometry("1500x850")
        self.root.title("insta")
        for widget in self.root.winfo_children():
            widget.destroy()
        self.face_image = PhotoImage(file='face.png')
        self.home_image = PhotoImage(file='home page.png')
        self.personal_image = PhotoImage(file='personal.png')
        self.add_image = PhotoImage(file='add.png')
        self.setting_image = PhotoImage(file='setting.png')
        self.insta_image = PhotoImage(file='insta.png')
        self.search_image = PhotoImage(file='search.png')
        self.x = 0
        self.y = 0
        self.main_frame = Frame(self.root, bg="white", width=300, height=680,relief="raised")
        self.main_frame.place(x=550, y=10)

        self.futures_frame = Frame(self.main_frame, bg="white", width=300, height=25, relief="flat")
        self.futures_frame.columnconfigure(self.x, weight=1)
        self.futures_frame.place(y=635)
        self.label_frame = Frame(self.main_frame, bg="white", width=300, height=30, relief="flat")
        self.label_frame.place(y=0)
        self.name_label = Label(self.label_frame, image=self.insta_image, bg="white")
        self.name_label.pack()
        self.user_frame = Frame(self.main_frame, bg="white", width=300, height=40)
        self.user_frame.columnconfigure(self.x, weight=1)
        self.user_frame.place(y=65)
        self.stats_frame = Frame(self.main_frame, bg="white")
        self.stats_frame.columnconfigure(self.x, weight=1)
        self.stats_frame.place(x=40,y=200)
        self.posts_label = Label(self.stats_frame, text="Posts\n0", font=("Helvetica", 10), bg="white")
        self.posts_label.pack(side=tkinter.LEFT, padx=10)
        self.followers_label = Label(self.stats_frame, text="Followers\n0", font=("Helvetica", 10), bg="white")
        self.followers_label.pack(side=tkinter.LEFT, padx=10)
        self.following_label = Label(self.stats_frame, text="Following\n0", font=("Helvetica", 10), bg="white")
        self.following_label.pack(side=tkinter.LEFT, padx=10)
        self.edit_button = Button(self.main_frame,relief=FLAT ,text="Edit Profile", font=("Helvetica", 10), width=7)
        self.edit_button.place(x=100,y=80)
        self.archive_button = Button(self.main_frame, relief=FLAT, text="View Archive", font=("Helvetica", 10), width=10)
        self.archive_button.place(x=200, y=80)
        self.share_frame=Frame(self.main_frame, bg="white")
        self.share_frame.place(x=30,y=300)
        self.share_label=Label(self.share_frame,text="Share Photos",font=("Helvetica",20),width=10, bg="white")
        self.share_label.pack()
        self.ph_label=Label(self.share_frame,text="when you share photos,they will appear\n on your profile",
                            font=("Helvetica",10),width=30, bg="white")

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

        home_page = Button(self.futures_frame, image=self.home_image, borderwidth=0, bg="white",command=self.back_click)
        home_page.grid(row=0, column=1, padx=25)

    def btn_user(self):
        self.x += 1
        button_image = Button(self.user_frame, image=self.face_image, borderwidth=0, text="user name",
                              font=("Arial", 10), compound=tkinter.TOP, bg="white")
        button_image.grid(row=0, column=self.x, padx=5)

    def back_click(self):
        Home_page(self.root)
class others():
    def __init__(self,root):
        self.root = Tk()
        self.root = root
        self.root.geometry("1500x850")
        self.root.title("insta")
        for widget in self.root.winfo_children():
            widget.destroy()
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
        self.posts_label.pack(side=tkinter.LEFT, padx=10)
        self.followers_label = Label(self.stats_frame, text="Followers\n100", font=("Helvetica", 10), bg="white")
        self.followers_label.pack(side=tkinter.LEFT, padx=10)
        self.following_label = Label(self.stats_frame, text="Following\n200", font=("Helvetica", 10), bg="white")
        self.following_label.pack(side=tkinter.LEFT, padx=10)
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

        home_page = Button(self.futures_frame, image=self.home_image, borderwidth=0, bg="white",command=self.back_click)
        home_page.grid(row=0, column=1, padx=25)

    def btn_user(self):
        self.x += 1
        button_image = Button(self.user_frame, image=self.face_image, borderwidth=0, text="sohaila esam",
                              font=("Arial", 10), compound=tkinter.TOP, bg="white")
        button_image.grid(row=0, column=self.x, padx=5)
    def back_click(self):
        Home_page(self.root)
    def chat_click(self):
        Chat(self.root)

class Chat:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x680")
        self.root.configure(bg="white")
        for widget in self.root.winfo_children():
            widget.destroy()

        self.stack = Stack()

        self.frame = Frame(self.root, bg="white")
        self.frame.pack(pady=10)

        self.display_frame = Frame(self.frame, bg="white")
        self.display_frame.pack()

        self.input_frame = Frame(self.frame, bg="white")
        self.input_frame.pack(side=BOTTOM)

        self.post_entry = Text(self.input_frame, width=30, height=5)
        self.post_entry.pack(side=LEFT, pady=5)

        self.button_frame = Frame(self.input_frame, bg="white")
        self.button_frame.pack(side=LEFT, padx=5)

        self.post_button = Button(self.button_frame, text="Send", command=self.send_message, bg="black", fg="white")
        self.post_button.pack(pady=5)

        self.delete_button = Button(self.button_frame, text="Delete", command=self.delete_message, bg="black", fg="white")
        self.delete_button.pack(pady=5)

    def send_message(self):
        new_message = self.post_entry.get("1.0", END).strip()
        if new_message:
            self.stack.push(new_message)
            self.post_entry.delete("1.0", END)
            self.display_messages()

    def delete_message(self):
        message = self.stack.pop()
        if message:
            self.display_messages()

    def display_messages(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        all_messages = self.stack.peek()
        if all_messages is not None:
            for message in all_messages:
                message_label = Label(self.display_frame, text=message, wraplength=300, bg="white")
                message_label.pack(pady=5)

    def back_click(self):
        Home_page(self.root)

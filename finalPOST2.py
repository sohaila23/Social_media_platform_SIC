from stack import Stack
from tkinter import *

class Posts:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x680")
        self.root.configure(bg="white")

        self.stack = Stack()

        self.frame = Frame(self.root, bg="white")
        self.frame.pack(pady=10)

        self.input_frame = Frame(self.frame, bg="white")
        self.input_frame.pack()

        self.post_entry = Text(self.input_frame, width=30, height=5)
        self.post_entry.pack(side="left")

        self.button_frame = Frame(self.input_frame, bg="white")
        self.button_frame.pack(side="left")

        self.post_button = Button(self.button_frame, text="Publish", command=self.make_post, bg="black", fg="white")
        self.post_button.pack(pady=5)

        self.delete_post_button = Button(self.button_frame, text="Delete", command=self.delete_post, bg="black", fg="white")
        self.delete_post_button.pack(pady=5)

        self.display_frame = Frame(self.frame, bg="white")
        self.display_frame.pack()

    def make_post(self):
        new_post = self.post_entry.get("1.0", END).strip()
        if new_post:
            self.stack.push(new_post)
            self.post_entry.delete("1.0", END)
            self.display_posts()

    def delete_post(self):
        post = self.stack.pop()
        if post:
            self.display_posts()

    def display_posts(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        all_posts = self.stack.peek()
        if all_posts is not None:
            for post in all_posts:
                post_label = Label(self.display_frame, text=post, wraplength=300, bg="white")
                post_label.pack(pady=5)

#root = Tk()
#POST = Posts(root)
#root.mainloop()
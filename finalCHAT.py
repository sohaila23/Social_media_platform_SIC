from stack import Stack
from tkinter import *

class Chat:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x680")
        self.root.configure(bg="white")

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

#root = Tk()
#CHAT = Chat(root)
#root.mainloop()
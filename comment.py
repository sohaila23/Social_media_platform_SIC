from queue1 import Queue
from tkinter import *
# from Home import Home_page
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
    # def back_click(self):
        # Home_page(self.root)
    def display_messages(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        all_messages = self.queue.peek()
        if all_messages is not None:
            for message in all_messages:
                message_label = Label(self.display_frame, text=message, wraplength=300, bg="white")
                message_label.pack(pady=5)

#CHAT = Chat(root)
#root.mainloop()
#root = Tk()
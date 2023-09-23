'''import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import *


class UserProfilePage:
    def __init__(self, root):
        self.root = root
        self.root.title("User Profile Page")
        self.root.geometry("1600x1000")
        self.root.configure(bg="black")
        self.friends = []

        # Create variables to store user information
        self.username = tk.StringVar()
        self.profile_picture = tk.StringVar()
        self.bio = tk.StringVar()

        # Create labels and entry fields for user information
        tk.Label(root, text=f"Welcome, {self.username}!", bg="black", fg='LightBlue1',
                 font=("arial", 20, "bold")).pack(pady=10)

        '''self.friend_entry = tk.Entry(root, width=30)
        self.friend_entry.pack()
        send_request_button = tk.Button(root, text="Send Friend Request", command=self.send_friend_request)
        send_request_button.pack()

        tk.Label(root, text="Friends:").pack()
        self.friends_listbox = tk.Listbox(root, width=30)
        self.friends_listbox.pack()

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_request, state="disabled")
        self.reject_button = tk.Button(root, text="Reject", command=self.reject_request, state="disabled")
        self.friends_listbox.bind("<<ListboxSelect>>", self.update_buttons)'''
        self.friend_label = tk.Label(root, text="Friend:")
        self.friend_entry = tk.Entry(root)
        self.send_button = tk.Button(root, text="Send Friend Request", command=self.send_friend_request)

        self.friends_label = tk.Label(root, text="Friends:")
        self.friends_listbox = tk.Listbox(root)
        self.friends_listbox.bind('<<ListboxSelect>>', self.update_buttons)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_request, state="disabled")
        self.reject_button = tk.Button(root, text="Reject", command=self.reject_request, state="disabled")

        # Add GUI elements to the layout
        self.friend_label.place(x=200,y=300)
        self.friend_entry.place(x=250,y=350)
        self.send_button.place(x=400,y=400)

        self.friends_label.place(x=100, y=150)
        self.friends_listbox.place(x=150,y=200)
        self.accept_button.place(x=200,y=350)
        self.reject_button.place(x=400,y=500)

        tk.Label(root, text="Username:", bg="black", fg='LightBlue1',
                 font=("arial", 20, "bold")).place(x=600, y=180)
        self.username_entry = tk.Entry(root, textvariable=self.username, width=25, border=0, highlightthickness=0,
                                       relief=FLAT, fg='white', bg='black', font=('yu gothic wi', 11, "bold"))
        self.username_entry.place(x=600, y=220)

        tk.Label(root, text="Profile Picture:", bg="black", fg='LightBlue1',
                 font=("arial", 20, "bold")).place(x=600, y=240)
        self.profile_picture_entry = tk.Entry(root, textvariable=self.profile_picture, state="disabled", width=25,
                                              border=0, highlightthickness=0, relief=FLAT, fg='white', bg='black',
                                              font=('yu gothic wi', 11, "bold"))
        self.profile_picture_entry.place(x=600, y=280)
        self.profile_picture_button = tk.Button(root, text="Browse", command=self.browse_profile_picture, width=20,
                                                cursor='hand2', bg="LightBlue1", fg="black",
                                                font=('yu gothic wi', 13, "bold"), activebackground='LightBlue1')

        self.profile_picture_button.place(x=850, y=275)

        tk.Label(root, text="Bio:", bg="black", fg='LightBlue1',
                 font=("arial", 20, "bold")).place(x=600, y=300)
        self.bio_entry = tk.Entry(root, textvariable=self.bio, width=25, border=0, highlightthickness=0, relief=FLAT,
                                  fg='white', bg='black', font=('yu gothic wi', 11, "bold"))
        self.bio_entry.place(x=600, y=340)

        # Create buttons for saving and updating the profile
        save_button = tk.Button(root, text="Save Profile", command=self.save_profile, width=20, cursor='hand2',
                                bg="LightBlue1", fg="black", font=('yu gothic wi', 13, "bold"),
                                activebackground='LightBlue1')
        save_button.place(x=550, y=380)

        update_button = tk.Button(root, text="Update Profile", command=self.update_profile, width=20, cursor='hand2',
                                  bg="LightBlue1", fg="black", font=('yu gothic wi', 13, "bold"),
                                  activebackground='LightBlue1')
        update_button.place(x=800, y=380)

        # Load user profile if available
        self.load_profile()

    def browse_profile_picture(self):
        # Open file dialog to select profile picture
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if filename:
            self.profile_picture.set(filename)
            self.display_profile_picture(filename)

    def display_profile_picture(self, filename):
        # Load the image file and display it in the picture entry
        image = tk.PhotoImage(file=filename)
        self.profile_picture_entry.configure(state="normal")
        self.profile_picture_entry.delete(0, tk.END)
        self.profile_picture_entry.image = image
        self.profile_picture_entry.insert(tk.END, filename)
        self.profile_picture_entry.configure(state="disabled")

    def save_profile(self):
        # Save user profile information
        # Here, you can implement the logic to save the information to a file or database
        messagebox.showinfo("Save Profile", "Profile saved successfully!")

    def update_profile(self):
        '''update_dialog = UpdateProfileDialog(self.root, self.username.get(), self.profile_picture.get(), self.bio.get())
        self.root.wait_window(update_dialog.top)

        if update_dialog.result:
            # Update user profile with the changes
            self.username.set(update_dialog.username)
            self.profile_picture.set(update_dialog.profile_picture)
            self.bio.set(update_dialog.bio)
            messagebox.showinfo("Update Profile", "Profile updated successfully!")'''

        messagebox.showinfo("Update Profile", "Profile updated successfully!")

    def load_profile(self):
        # Load user profile information
        # Here, you can implement the logic to load the information from a file or database
        # For demonstration purposes, let's assume some default values
        self.username.set("JohnDoe")
        self.bio.set("I'm a Python developer.")

    def send_friend_request(self):
        friend_username = self.friend_entry.get()
        if friend_username:
            if friend_username == self.username.get():
                messagebox.showerror("Error", "You cannot send a friend request to yourself.")
            elif friend_username in self.friends:
                messagebox.showerror("Error", "You are already friends with this user.")
            else:
                # Simulate sending a friend request (you would add logic to handle requests)
                messagebox.showinfo("Friend Request Sent", f"Friend request sent to {friend_username}.")
                self.friends_listbox.insert(tk.END, friend_username)
                self.friend_entry.delete(0, tk.END)

    def accept_request(self):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            # Simulate accepting a friend request (you would add logic to handle requests)
            messagebox.showinfo("Friend Request Accepted", f"You are now friends with {selected_friend}.")
            self.friends.append(selected_friend)
            self.friends_listbox.delete(tk.ACTIVE)
            self.update_buttons()

    def reject_request(self):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            # Simulate rejecting a friend request (you would add logic to handle requests)
            messagebox.showinfo("Friend Request Rejected",
                                f"You have rejected the friend request from {selected_friend}.")
            self.friends_listbox.delete(tk.ACTIVE)
            self.update_buttons()

    def update_buttons(self, event=None):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            self.accept_button.config(state="normal")
            self.reject_button.config(state="normal")
        else:
            self.accept_button.config(state="disabled")
            self.reject_button.config(state="disabled")

    ''' def send_friend_request(self):
        friend_username = self.friend_entry.get()
        if friend_username:
            if friend_username == self.username:
                messagebox.showerror("Error", "You cannot send a friend request to yourself.")
            elif friend_username in self.friends:
                messagebox.showerror("Error", "You are already friends with this user.")
            else:
                # Simulate sending a friend request (you would add logic to handle requests)
                messagebox.showinfo("Friend Request Sent", f"Friend request sent to {friend_username}.")

    def accept_request(self):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            # Simulate accepting a friend request (you would add logic to handle requests)
            messagebox.showinfo("Friend Request Accepted", f"You are now friends with {selected_friend}.")
            self.friends.append(selected_friend)
            self.friends_listbox.delete(tk.ACTIVE)
            self.update_buttons()

    def reject_request(self):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            # Simulate rejecting a friend request (you would add logic to handle requests)
            messagebox.showinfo("Friend Request Rejected",
                                f"You have rejected the friend request from {selected_friend}.")
            self.friends_listbox.delete(tk.ACTIVE)
            self.update_buttons()

    def update_buttons(self, event=None):
        selected_friend = self.friends_listbox.get(tk.ACTIVE)
        if selected_friend:
            self.accept_button.config(state="normal")
            self.reject_button.config(state="normal")
        else:
            self.accept_button.config(state="disabled")
            self.reject_button.config(state="disabled")'''


'''class UpdateProfileDialog:
    def __init__(self, parent, username, profile_picture, bio):
        self.top = tk.Toplevel(parent)
        self.top.title("Update Profile")
        self.result = False

        # Create variables to store user information
        self.username = tk.StringVar()
        self.profile_picture = tk.StringVar()
        self.bio = tk.StringVar()

        # Set initial values
        self.username.set(username)
        self.profile_picture.set(profile_picture)
        self.bio.set(bio)

        # Create labels and entry fields for user information in the dialog
        tk.Label(self.top, text="Username:").pack()
        self.username_entry = tk.Entry(self.top, textvariable=self.username)
        self.username_entry.pack()

        tk.Label(self.top, text="Profile Picture URL:").pack()
        self.profile_picture_entry = tk.Entry(self.top, textvariable=self.profile_picture)
        self.profile_picture_entry.pack()

        tk.Label(self.top, text="Bio:").pack()
        self.bio_entry = tk.Entry(self.top, textvariable=self.bio)
        self.bio_entry.pack()

        # Create "Save" and "Cancel" buttons
        save_button = tk.Button(self.top, text="Save", command=self.save)
        save_button.pack()
        cancel_button = tk.Button(self.top, text="Cancel", command=self.cancel)
        cancel_button.pack()

    def save(self):
        self.result = True
        self.top.destroy()

    def cancel(self):
        self.top.destroy()
'''

# Create the main window
root = tk.Tk()

# Create the user profile page
profile_page = UserProfilePage(root)

# Start the Tkinter event loop
root.mainloop()
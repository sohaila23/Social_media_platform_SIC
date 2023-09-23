import tkinter as tk
from tkinter import messagebox


# User class to represent a user and their profile
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.profile = Profile()
        self.friend_requests = []
        self.friends = []

    def send_friend_request(self, user):
        user.friend_requests.append(self)
        messagebox.showinfo('Friend Request', f'Friend request sent to {user.username}.')

    def accept_friend_request(self, user):
        if user in self.friend_requests:
            self.friend_requests.remove(user)
            self.friends.append(user)
            user.friends.append(self)
            messagebox.showinfo('Friend Request', f'Friend request from {user.username} accepted.')
        else:
            messagebox.showerror('Friend Request', 'Invalid friend request.')

    def reject_friend_request(self, user):
        if user in self.friend_requests:
            self.friend_requests.remove(user)
            messagebox.showinfo('Friend Request', f'Friend request from {user.username} rejected.')
        else:
            messagebox.showerror('Friend Request', 'Invalid friend request.')


# Profile class to represent a user's profile
class Profile:
    def __init__(self):
        self.profile_picture = ''  # File path to the profile picture
        self.bio = ''  # User's bio


# Function to register a new user
def register():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are not empty
    if username and password:
        # Check if the username is not already taken
        if username not in users:
            # Create a new user instance and add it to the users dictionary
            user = User(username, password)
            users[username] = user
            messagebox.showinfo('Registration', 'Registration successful!')
            show_profile_page(user)
        else:
            messagebox.showerror('Registration', 'Username already exists.')
    else:
        messagebox.showerror('Registration', 'Please enter a username and password.')


# Function to handle user login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match
    if username in users:
        user = users[username]
        if user.password == password:
            messagebox.showinfo('Login', 'Login successful!')
            show_profile_page(user)
            return

    messagebox.showerror('Login', 'Invalid username or password.')


# Function to display the profile page for a user
def show_profile_page(user):
    window.withdraw()  # Hide the main window

    profile_window = tk.Toplevel()  # Create a new window for the profile page
    profile_window.title('Profile Page')
    profile_window.configure(bg='#F8F8F8')  # Set background color

    # Create and position the profile picture label and entry
    profile_picture_label = tk.Label(profile_window, text='Profile Picture:', bg='#F8F8F8', fg='#333333',
                                     font=('Arial', 14, 'bold'))
    profile_picture_label.pack()
    profile_picture_entry = tk.Entry(profile_window, width=30)
    profile_picture_entry.pack()

    # Create and position the bio label and entry
    bio_label = tk.Label(profile_window, text='Bio:', bg='#F8F8F8', fg='#333333', font=('Arial', 14, 'bold'))
    bio_label.pack()
    bio_entry = tk.Entry(profile_window, width=30)
    bio_entry.pack()

    # Function to update the profile picture
    def update_profile_picture():
        user.profile.profile_picture = profile_picture_entry.get()
        messagebox.showinfo('Profile Update', 'Profile picture updated.')

    # Function to update the bio
    def update_bio():
        user.profile.bio = bio_entry.get()
        messagebox.showinfo('Profile Update', 'Bio updated.')

    # Create and position the update buttons
    update_picture_button = tk.Button(profile_window, text='Update Picture', command=update_profile_picture,
                                      bg='#4CAF50', fg='#FFFFFF', font=('Arial', 12, 'bold'))
    update_picture_button.pack(pady=10)
    update_bio_button = tk.Button(profile_window, text='Update Bio', command=update_bio, bg='#4CAF50', fg='#FFFFFF',
                                  font=('Arial', 12, 'bold'))
    update_bio_button.pack(pady=10)

    # Function to handle sending a friend request
    def send_friend_request(friend_request_entry=None):
        recipient_username = friend_request_entry.get()
        
        if recipient_username in users:
            recipient = users[recipient_username]
            user.send_friend_request(recipient)
        else:
            messagebox.showerror('Friend Request', 'Invalid recipient username.')

    # FunctionThis is a code snippet written in Python using the Tkinter library for creating a GUI. To make the pages more colorful and beautiful, you can customize the colors, fonts, and styles used in the interface. Here's an example of how you can modify the code to make the pages more visually appealing:


# Create the main window
window = tk.Tk()
window.title('User Login')
window.configure(bg='#F8F8F8')  # Set background color
users={}
# Create and position the username label and entry
username_label = tk.Label(window, text='Username:', bg='#F8F8F8', fg='#333333', font=('Arial', 14, 'bold'))
username_label.pack()
username_entry = tk.Entry(window, width=30)
username_entry.pack()

# Create and position the password label and entry
password_label = tk.Label(window, text='Password:', bg='#F8F8F8', fg='#333333', font=('Arial', 14, 'bold'))
password_label.pack()
password_entry = tk.Entry(window, width=30, show='*')
password_entry.pack()

# Create and position the login button
login_button = tk.Button(window, text='Login', command=login, bg='#4CAF50', fg='#FFFFFF', font=('Arial', 12, 'bold'))
login_button.pack(pady=10)

# Create and position the register button
register_button = tk.Button(window, text='Register', command=register, bg='#4CAF50', fg='#FFFFFF',
                            font=('Arial', 12, 'bold'))
register_button.pack(pady=10)

# Run the main window loop
window.mainloop()

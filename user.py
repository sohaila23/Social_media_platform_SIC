import tkinter as tk
from tkinter import messagebox


# Dummy user profile data
user_profiles = {
    "user1": {
        "username": "user1",
        "email": "user1@example.com",
        "profile_picture": "default.png",
        "bio": "This is my bio.",
        "personal_details": "Age: 25, Location: New York"
    }
}

# Function to update user profile
def update_profile():
    username = username_entry.get()
    profile_picture = profile_picture_entry.get()
    bio = bio_entry.get("1.0", "end-1c")  # Get bio text from the text widget
    personal_details = personal_details_entry.get()

    # Update the user's profile data
    user_profiles[username] = {
        "username": username,
        "email": user_profiles[username]['email'],
        "profile_picture": profile_picture,
        "bio": bio,
        "personal_details": personal_details
    }

    messagebox.showinfo("Success", "Profile updated successfully.")

# Create the main window
root = tk.Tk()
root.title("User Profile")

# Retrieve the username from the login session (you should implement this in your application)
current_username = ""

# Create labels
username_label = tk.Label(root, text="Username:")
profile_picture_label = tk.Label(root, text="Profile Picture URL:")
bio_label = tk.Label(root, text="Bio:")
personal_details_label = tk.Label(root, text="Personal Details:")

# Create entry fields and text widget
username_entry = tk.Entry(root, state="readonly")
profile_picture_entry = tk.Entry(root)
bio_entry = tk.Text(root, height=5, width=40)
personal_details_entry = tk.Entry(root)

# Populate fields with user's current profile data
user_data = user_profiles.get(current_username, {})
username_entry.insert(0, user_data.get("username", ""))
profile_picture_entry.insert(0, user_data.get("profile_picture", ""))
bio_entry.insert("1.0", user_data.get("bio", ""))
personal_details_entry.insert(0, user_data.get("personal_details", ""))

# Create a button to update the profile
update_button = tk.Button(root, text="Update Profile", command=update_profile)

# Place widgets on the grid
username_label.grid(row=0, column=0)
profile_picture_label.grid(row=1, column=0)
bio_label.grid(row=2, column=0)
personal_details_label.grid(row=3, column=0)

username_entry.grid(row=0, column=1)
profile_picture_entry.grid(row=1, column=1)
bio_entry.grid(row=2, column=1)
personal_details_entry.grid(row=3, column=1)

update_button.grid(row=4, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()

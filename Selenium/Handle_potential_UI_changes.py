import tkinter as tk
def create_login_page(root):
    root.title("Facebook Login Page Simulation")
    root.geometry("400x300")

    login_label = tk.Label(root, text="Email or Phone")   # Create and place the login label
    login_label.pack(pady=(50, 5))

    login_entry = tk.Entry(root)  # Create and place the login entry
    login_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password") # Create and place the password label
    password_label.pack(pady=5)

    password_entry = tk.Entry(root, show="*")  # Create and place the password entry
    password_entry.pack(pady=5)

    login_button = tk.Button(root, text="Log In")  # Create the login button
    login_button.pack(pady=(20, 5))

    forgot_password_link = tk.Label(root, text="Forgot Password?", fg="blue", cursor="hand2")
    forgot_password_link.pack(pady=(5, 20))     # Create the forgot password link

    def on_resize(event):   # Get the current width and height of the window
        width = event.width
        height = event.height

        # Calculate the new position for the login button and forgot password link (dynamic calculation)
        button_x = width // 2 - login_button.winfo_width() // 2
        link_x = width // 2 - forgot_password_link.winfo_width() // 2

        # Keep a fixed offset from the top for the login button and an offset below it for the forgot password link
        button_y = height // 2 - 20
        link_y = button_y + 40  # Offset below the login button

        login_button.place(x=button_x, y=button_y)     # Move the login button and forgot password link to the new positions
        forgot_password_link.place(x=link_x, y=link_y)
       
    root.bind("<Configure>", on_resize)  # Bind the resize event to a callback function

def main():
    root = tk.Tk()
    create_login_page(root)
    root.mainloop()

if __name__ == "__main__":
    main()

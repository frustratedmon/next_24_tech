import tkinter as tk
from tkinter import messagebox

def submit():
   
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    messagebox.showinfo("Submitted Information", f"Name: {name}\nEmail: {email}\nAge: {age}")

root = tk.Tk()
root.title("Registration Form")
root.configure(bg="lightblue")

label_name = tk.Label(root, text="Enter Your Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Enter Your Email:")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Enter Your Age:")
label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

button_submit = tk.Button(root, text="Submit Button", command=submit,bg='red', fg='white')
button_submit.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()

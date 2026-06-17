import tkinter as tk
from tkinter import messagebox
import random
import string


# -----------------------------
# Generate Password
# -----------------------------
def generate_password():
    chars = ""

    if upper_var.get():
        chars += string.ascii_uppercase

    if lower_var.get():
        chars += string.ascii_lowercase

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning(
            "Warning",
            "Select at least one character type."
        )
        return

    length = length_scale.get()

    password = "".join(
        random.choice(chars)
        for _ in range(length)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    update_strength(length)


# -----------------------------
# Password Strength
# -----------------------------
def update_strength(length):
    if length < 8:
        strength_label.config(text="Strength: Weak", fg="#E63946")
    elif length < 14:
        strength_label.config(text="Strength: Medium", fg="#F4A261")
    else:
        strength_label.config(text="Strength: Strong", fg="#2A9D8F")


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x420")
root.resizable(False, False)

# Background Color
root.configure(bg="#EAF4F4")

# -----------------------------
# Heading
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 20, "bold"),
    bg="#EAF4F4",
    fg="#1D3557"
)
title.pack(pady=15)

# -----------------------------
# Password Box
# -----------------------------
password_entry = tk.Entry(
    root,
    font=("Consolas", 14),
    justify="center",
    width=35,
    bd=2
)
password_entry.pack(pady=10)

# -----------------------------
# Length Section
# -----------------------------
length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 11),
    bg="#EAF4F4",
    fg="#1D3557"
)
length_label.pack()

length_scale = tk.Scale(
    root,
    from_=4,
    to=32,
    orient="horizontal",
    length=250,
    bg="#EAF4F4",
    highlightthickness=0
)
length_scale.set(12)
length_scale.pack()

# -----------------------------
# Options
# -----------------------------
options_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)
options_frame.pack(pady=15)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    options_frame,
    text="Uppercase",
    variable=upper_var,
    bg="#EAF4F4"
).grid(row=0, column=0, padx=10)

tk.Checkbutton(
    options_frame,
    text="Lowercase",
    variable=lower_var,
    bg="#EAF4F4"
).grid(row=0, column=1, padx=10)

tk.Checkbutton(
    options_frame,
    text="Numbers",
    variable=number_var,
    bg="#EAF4F4"
).grid(row=1, column=0, padx=10)

tk.Checkbutton(
    options_frame,
    text="Symbols",
    variable=symbol_var,
    bg="#EAF4F4"
).grid(row=1, column=1, padx=10)

# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)
button_frame.pack(pady=15)

generate_btn = tk.Button(
    button_frame,
    text="Generate Password",
    width=18,
    bg="#457B9D",
    fg="white",
    activebackground="#1D3557",
    activeforeground="white",
    command=generate_password
)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(
    button_frame,
    text="Copy Password",
    width=18,
    bg="#2A9D8F",
    fg="white",
    activebackground="#1F776D",
    activeforeground="white",
    command=copy_password
)
copy_btn.grid(row=0, column=1, padx=10)

# -----------------------------
# Strength Label
# -----------------------------
strength_label = tk.Label(
    root,
    text="Strength: -",
    font=("Arial", 11, "bold"),
    bg="#EAF4F4",
    fg="#1D3557"
)
strength_label.pack(pady=10)

# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="Created with Python & Tkinter",
    font=("Arial", 9),
    bg="#EAF4F4",
    fg="#555555"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
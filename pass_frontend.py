import random
import tkinter as tk
from tkinter import messagebox

# Character set from your original code
CHARS = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"


def generate_password():
    raw_length = length_entry.get().strip()
    try:
        length = int(raw_length)
    except ValueError:
        messagebox.showerror("Invalid length", "Enter a whole number, for example 12 or 16.")
        length_entry.focus_set()
        return

    if not 1 <= length <= 256:
        messagebox.showerror("Invalid length", "Choose a length between 1 and 256.")
        return

    password = "".join(random.choice(CHARS) for _ in range(length))
    password_var.set(password)
    status_var.set(f"Password generated • {length} characters")


def copy_password():
    password = password_var.get()
    if not password:
        messagebox.showinfo("Nothing to copy", "Generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    status_var.set("Password copied to clipboard.")


def clear_password():
    password_var.set("")
    status_var.set("Enter a length and generate a new password.")
    length_entry.focus_set()


root = tk.Tk()
root.title("PassCraft | Password Suggestion")
root.geometry("780x560")
root.minsize(650, 500)
root.configure(bg="#0b1020")

BG, PANEL, FIELD = "#0b1020", "#121a2d", "#0c1425"
TEXT, MUTED, PURPLE, TEAL, BORDER = "#eef3ff", "#9caac5", "#7c5cff", "#23c9a8", "#293650"

header = tk.Frame(root, bg="#211b4b", padx=28, pady=24)
header.pack(fill="x", padx=18, pady=(18, 12))

brand = tk.Frame(header, bg="#211b4b")
brand.pack(anchor="w")
tk.Label(brand, text="🔐", font=("Segoe UI Emoji", 22), bg="#211b4b", fg=TEXT).pack(side="left", padx=(0, 10))
tk.Label(brand, text="PassCraft", font=("Segoe UI", 18, "bold"), bg="#211b4b", fg=TEXT).pack(side="left")
tk.Label(header, text="PASSWORD SUGGESTION TOOL", font=("Segoe UI", 9, "bold"), bg="#211b4b", fg="#b8b1ff").pack(anchor="w", pady=(18, 6))
tk.Label(header, text="Create a strong, random password.", font=("Segoe UI", 20, "bold"), bg="#211b4b", fg=TEXT).pack(anchor="w")
tk.Label(header, text="Choose the length, generate, then copy it in one click.", font=("Segoe UI", 10), bg="#211b4b", fg="#c2cce0").pack(anchor="w", pady=(7, 0))

card = tk.Frame(root, bg=PANEL, padx=28, pady=24, highlightbackground=BORDER, highlightthickness=1)
card.pack(fill="both", expand=True, padx=18, pady=(0, 18))

tk.Label(card, text="Create your password", font=("Segoe UI", 15, "bold"), bg=PANEL, fg=TEXT).pack(anchor="w")
tk.Label(card, text="PASSWORD LENGTH", font=("Segoe UI", 9, "bold"), bg=PANEL, fg=MUTED).pack(anchor="w", pady=(20, 7))

length_row = tk.Frame(card, bg=PANEL)
length_row.pack(fill="x")
length_entry = tk.Entry(length_row, font=("Segoe UI", 13), bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat", highlightthickness=1, highlightbackground=BORDER, highlightcolor=PURPLE, width=12)
length_entry.pack(side="left", ipady=10, ipadx=10)
length_entry.insert(0, "16")
tk.Label(length_row, text="Recommended: 12–20 characters", font=("Segoe UI", 9), bg=PANEL, fg=MUTED).pack(side="left", padx=14)

tk.Label(card, text="YOUR SUGGESTED PASSWORD", font=("Segoe UI", 9, "bold"), bg=PANEL, fg=MUTED).pack(anchor="w", pady=(22, 8))
password_var = tk.StringVar()
password_entry = tk.Entry(card, textvariable=password_var, font=("Consolas", 13), bg=FIELD, fg=TEAL, insertbackground=TEXT, relief="flat", highlightthickness=1, highlightbackground=BORDER, readonlybackground=FIELD, state="readonly")
password_entry.pack(fill="x", ipady=12)

button_row = tk.Frame(card, bg=PANEL)
button_row.pack(fill="x", pady=(16, 0))
tk.Button(button_row, text="✦  Generate password", command=generate_password, font=("Segoe UI", 10, "bold"), bg=PURPLE, fg="white", activebackground="#6a4be8", activeforeground="white", relief="flat", cursor="hand2", padx=18, pady=12).pack(side="left")
tk.Button(button_row, text="Copy password", command=copy_password, font=("Segoe UI", 10, "bold"), bg="#203149", fg=TEXT, activebackground="#2b405d", activeforeground=TEXT, relief="flat", cursor="hand2", padx=18, pady=12).pack(side="left", padx=(10, 0))
tk.Button(button_row, text="Clear", command=clear_password, font=("Segoe UI", 10), bg=PANEL, fg=MUTED, activebackground=PANEL, activeforeground=TEXT, relief="flat", cursor="hand2", padx=14, pady=12).pack(side="left", padx=(5, 0))

status_var = tk.StringVar(value="Enter a length and generate a new password.")
tk.Label(card, textvariable=status_var, font=("Segoe UI", 9), bg=PANEL, fg=TEAL, anchor="w").pack(fill="x", pady=(14, 0))
tk.Label(card, text="Privacy tip: use a unique password for each account and store it in a trusted password manager.", font=("Segoe UI", 9), bg=PANEL, fg=MUTED, wraplength=680, justify="left").pack(anchor="w", pady=(18, 0))

root.bind("<Return>", lambda event: generate_password())
length_entry.focus_set()
root.mainloop()

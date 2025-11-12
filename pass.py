import tkinter as tk
from tkinter import messagebox
import re

def check():
    score = 0
    ch = lbox.get()
    msg = []

    if not ch:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    
    #length
    len_ch = len(ch)
    if len_ch <8:
        msg.append("Use at least 8 characters.")
    elif 8 <= len_ch <12:
        score += 1
    else:
        score += 2
    
    #uppercase
    if re.search(r'[A-Z]', ch):
        score += 2
    else:
        msg.append("Add uppercase letters.")
    
    #lowercase
    if re.search(r'[a-z]', ch):
        score += 1
    else:
        msg.append("Add lowercase letters.")

    #digits
    if re.search(r'\d', ch):    
        score += 1
    else:
        msg.append("Add numbers.")

    #special
    if re.search(r'[@$!%*?&#]', ch):
        score += 2
    else:
        msg.append("Add special characters.")
    
    #result
    if score <= 3:
        s = "Weak"
        color = "red"
    elif 4 <= score <= 6:
        s = "Moderate"
        color = "orange"
    else:
        s = "Strong"
        color = "green"

    rl.config(text=f"Strength: {s}", fg=color)
    res = "\n".join(msg) if msg else "Looks good!"
    resl.config(text=res)

#mm
r = tk.Tk()
r.title("Password Checker")
r.geometry("400x300")
r.resizable(False, False)
r.configure(bg="#1E1E1E")
r.iconbitmap("key.ico")

tk.Label(r, text="🔑 Password Strength Checker", font=("Arial", 18, "bold"), fg="#769EDB", bg="#1E1E1E").pack(pady=10)

lbox = tk.StringVar()

frame = tk.Frame(r, bg="#1E1E1E")
frame.pack(pady=10)
tk.Label(frame, text="Enter Password:", fg="white", bg="#1E1E1E", font=("Arial", 14, "bold")).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=lbox, width=30, show="*").pack(side=tk.LEFT, padx=5)

    
tk.Button(r, text="Check Strength", command=check, bg="#769EDB", fg="black", font=("Arial", 12)).pack(pady=10)
rl = tk.Label(r, text="", font=("Arial", 14), fg="white", bg="#1E1E1E")
rl.pack(pady=5)
resl = tk.Label(r, text="", font=("Arial", 12), fg="white", bg="#1E1E1E")
resl.pack(pady=5)

tk.Label(r, text="© 2025 Abdelaziz Ounissi", fg="#769EDB", bg="#1E1E1E", font=("Arial", 8)).pack(side=tk.BOTTOM, pady=5)
r.mainloop()

    





    

    
import random
import tkinter as tk
from tkinter import messagebox


def show_password(password):
    messagebox.showinfo("Your password", password)


def generate_password(pass_len, lchoice, upchoice, numschoice, symschoice):
    lower_case = list('abcdefghijklmnopqrstuvwxyz')
    upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = list('0123456789')
    syms = list('!@#$%^&*()_-+=<>?~')
    options = []
    if lchoice == 1:
        options += lower_case
    if upchoice == 1:
        options += upper_case
    if numschoice == 1:
        options += nums
    if symschoice == 1:
        options += syms
    password = ""
    random_list = random.choices(options, k=pass_len)
    password = ''.join(map(str, random_list))
    show_password(password)

root = tk.Tk()
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
CheckVar3 = tk.IntVar()
CheckVar4 = tk.IntVar()
CheckVar5 = tk.IntVar()
w1 = tk.Label(root, text="Password Length: ", bg="black", fg="white")
w1.grid(row=0, column=0, sticky='nsew')
w2 = tk.Entry(root, textvariable=CheckVar5)
w2.grid(row=0, column=1)
w3 = tk.Checkbutton(root, text="Include lower-case", bg="black", fg="white", variable=CheckVar1)
w3.grid(row=1, column=0, columnspan=2, sticky='nsew')
w4 = tk.Checkbutton(root, text="Include upper-case", bg="black", fg="white", variable=CheckVar2)
w4.grid(row=2, column=0, columnspan=2, sticky='nsew')
w5 = tk.Checkbutton(root, text="Include numbers", bg="black", fg="white", variable=CheckVar3)
w5.grid(row=3, column=0, columnspan=2, sticky='nsew')
w6 = tk.Checkbutton(root, text="Include symbols", bg="black", fg="white", variable=CheckVar4)
w6.grid(row=4, column=0, columnspan=2, sticky='nsew')
#This button is weird, need lambda because passing a callback. Macs don't like background colors so it has to be a highlight
w7 = tk.Button(root, text="Generate Password", highlightbackground="red", command = lambda: generate_password(int(CheckVar5.get()), int(CheckVar1.get()), int(CheckVar2.get()), int(CheckVar3.get()), int(CheckVar4.get())))
w7.grid(row=5, column=0, columnspan=2, sticky='nsew')
tk.mainloop()
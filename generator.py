import random
import tkinter as tk
from tkinter import messagebox

#displays password in a new window
def show_password(password):
    messagebox.showinfo("Your password", password)


def too_long():
    messagebox.showinfo("Your password is too long", "Enter a password length of less than 20 characters")
        

def too_short():
    messagebox.showinfo("Your password is too short or negative", "Enter a password length greater than 0 characters")


def choose_a_box():
    messagebox.showinfo("You need to choose at least one checkbox", "Please select at least one category of characters and try again")


#leg work of generating the password
def generate_password(pass_len, lchoice, upchoice, numschoice, symschoice):
    #character banks
    lower_case = list('abcdefghijklmnopqrstuvwxyz')
    upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = list('0123456789')
    syms = list('!@#$%^&*()_-+=<>?~')
    options = []
    #if password length longer than 20 characters or 0 or less, return
    if pass_len <= 0:
        too_short()
        return
    if pass_len > 20:
        too_long()
        return

    #if no check boxes are checked, return
    if lchoice == 0 and upchoice == 0 and numschoice == 0 and symschoice == 0:
        choose_a_box()
        return
    #if the checkbox is checked, add the desired list to the overall bank
    if lchoice == 1:
        options += lower_case
    if upchoice == 1:
        options += upper_case
    if numschoice == 1:
        options += nums
    if symschoice == 1:
        options += syms
    #builds the password string
    password = ""
    random_list = random.choices(options, k=pass_len)
    password = ''.join(map(str, random_list))
    show_password(password)

#GUI
root = tk.Tk() #main frame
CheckVar1 = tk.IntVar() #checkbox and entry variables
CheckVar2 = tk.IntVar()
CheckVar3 = tk.IntVar()
CheckVar4 = tk.IntVar()
CheckVar5 = tk.IntVar()
w1 = tk.Label(root, text="Password Length: (20 characters or less)", bg="black", fg='#e5e5e5', relief=tk.RIDGE) 
w1.grid(row=0, column=0, sticky='nsew') #sticky fills the GUI box
w2 = tk.Entry(root, textvariable=CheckVar5)
w2.grid(row=0, column=1)
w3 = tk.Checkbutton(root, text="Include lower-case? (a, b, c, etc.)", bg="black", fg='#e5e5e5', variable=CheckVar1, justify=tk.LEFT)
w3.grid(row=1, column=0, columnspan=2, sticky='nsew')
w4 = tk.Checkbutton(root, text="Include upper-case? (A, B, C, etc.)", bg="black", fg='#e5e5e5', variable=CheckVar2, justify=tk.LEFT)
w4.grid(row=2, column=0, columnspan=2, sticky='nsew')
w5 = tk.Checkbutton(root, text="Include numbers? (1, 2, 3, etc)", bg="black", fg='#e5e5e5', variable=CheckVar3, justify=tk.LEFT)
w5.grid(row=3, column=0, columnspan=2, sticky='nsew')
w6 = tk.Checkbutton(root, text="Include symbols? (!, @, #, etc)", bg="black", fg='#e5e5e5', variable=CheckVar4, justify=tk.LEFT)
w6.grid(row=4, column=0, columnspan=2, sticky='nsew')
#This button is weird, need lambda because passing a callback. Macs don't like background colors so it has to be a highlight
w7 = tk.Button(root, text="Generate Password", highlightbackground="red", command = lambda: generate_password(int(CheckVar5.get()), int(CheckVar1.get()), int(CheckVar2.get()), int(CheckVar3.get()), int(CheckVar4.get())))
w7.grid(row=5, column=0, columnspan=2, sticky='nsew')
tk.mainloop()
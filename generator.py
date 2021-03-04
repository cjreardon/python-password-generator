import random


lower_case = list('abcdefghijklmnopqrstuvwxyz')
upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nums = list('0123456789')
syms = list('!@#$%^&*()_-+=<>?~')
password = ""
options = []

password_len = input("How many characters would you like your password to be? ")
while int(password_len) <= 0:
    password_len = input("Error! Password length must be larger than 0. Try again ")

lower_case_choice = input("Would you like to include lower case letters? (Y/N) ")
while lower_case_choice not in ["Y","N"]:
    lower_case_choice = input("Error! Please enter 'Y' or 'N' for a choice ")
if lower_case_choice == "Y":
    options += lower_case

upper_case_choice = input("Would you like to include upper case letters? (Y/N) ")
while upper_case_choice not in ["Y","N"]:
    upper_case_choice = input("Error! Please enter 'Y' or 'N' for a choice ")
if upper_case_choice == "Y":
    options += upper_case

nums_choice = input("Would you like to include numbers? (Y/N) ")
while nums_choice not in ["Y","N"]:
    nums_choice = input("Error! Please enter 'Y' or 'N' for a choice ")
if nums_choice == "Y":
    options += nums

syms_choice = input("Would you like to include symbols? (Y/N) ")
while syms_choice not in ["Y","N"]:
    syms_choice = input("Error! Please enter 'Y' or 'N' for a choice ")
if syms_choice == "Y":
    options += syms

random_list = random.choices(options, k=int(password_len))
password = ''.join(map(str, random_list))
print(password)
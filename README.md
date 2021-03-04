# python-password-generator
This script provides a GUI to generate a random password with your choice of letters, numbers, and symbols. I used Tkinter for the GUI. You can choose between upper case, lower case, numbers, and symbols to be in your password. You also select the password length (up to 20 characters). I used the built in python "random" library to choose from a bank of characters based on the user's preferences. There's error checking for when the user does not select a checkbox or enters a password length that is 0, negative, or too long.

This is an example of valid input:

<img width="425" alt="image" src="https://user-images.githubusercontent.com/80058871/110035344-89805a00-7d09-11eb-8783-0679f981a4cd.png">

And the result:

![image](https://user-images.githubusercontent.com/80058871/110035367-93a25880-7d09-11eb-98c9-d2f2ab75090c.png)


A bad user input (0 password length:

<img width="424" alt="Screen Shot 2021-03-04 at 4 50 32 PM" src="https://user-images.githubusercontent.com/80058871/110035480-bcc2e900-7d09-11eb-8c24-911f9c9d895e.png">

And the result:

<img width="253" alt="image" src="https://user-images.githubusercontent.com/80058871/110035574-d95f2100-7d09-11eb-95dc-2175c0e05c4e.png">

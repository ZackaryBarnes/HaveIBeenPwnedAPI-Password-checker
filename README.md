# HaveIBeenPwned-Password-checker
A simple program to interact with the HaveIBeenPwned API

# Instructions
The exe located in the dist folder will open a console window where you will be prompted to enter your password. Once you do the program will display how many times that password was involved in a data breach.

# K-Anonymity
The HaveIBeenPwned API uses K-Anonymity to protect the users data. The program sends only the first five characters of your hashed password to the API, the returned list of passwords is traversed to find the hash that matches the one belonging to your password. The only record of your password will be in the command line history which is cleared when you close the window.

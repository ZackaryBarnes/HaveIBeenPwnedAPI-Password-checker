import hashlib
import requests
from os import system, name
from time import sleep 

def main():
    clear()
    been_found = False
    number_of_times = 0
    plainText = input('Type in the password you would like to check: \n')
    hashed_pass = Hasher(plainText)
    clear()
    print("The hexadecimal equivalent of your password hased in SHA1 is:")
    print(hashed_pass) 
    shortend_hashed = (hashed_pass[:5])
    URL = f'https://api.pwnedpasswords.com/range/{shortend_hashed}'
    hash_list = requests.get(URL).text.split("\r\n")
    for hashes in hash_list:
        split_hash = hashes.split(":")
        if hashed_pass[5:] == split_hash[0]:
            number_of_times = split_hash[1]
            been_found = True

    PrintResults(been_found, number_of_times)
    input("Press ENTER to close")

def Hasher(password):
    hashed_version = hashlib.sha1(password.encode())
    return hashed_version.hexdigest().upper()

def PrintResults(been_found, number_of_times):
    if been_found == True:
        print("That password has been found", number_of_times, "times in data breaches \n")
    else:
        print("That password has not been found in any data breaches \n")

def clear(): 
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')

main()

#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Nov 15, 2022
# This program ask the user to enter the password to my account


def main():

    while True:
        # Get password and display if correct or not
        user_pass = input("Enter your password. (The password is 12345) : ")
        password = 12345
        try:
            user_pass_int = int(user_pass)
        except Exception:
            print("This is not the correct password")
            continue
        if user_pass_int > 12345:
            print("This is not the correct password")
            continue
        elif user_pass_int < 12345:
            print("This is not the correct password")
            continue
        while user_pass_int == password:
            print("Login successful")
            break
        break


if __name__ == "__main__":
    main()

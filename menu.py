import os
# from os import recipe-template.py

def menu():
print("\n\n\t\t\t'Welcome to Cookbook'\n")
choice = None
while choice != "0":
    print(""" Menu
        0 - Exit
        1 - Show Recipe Menu
        2 - Look Up Recipe
        3 - Add Recipe """)

    choice = input("Choice: ")
    print()
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        os.system('cls||clear')
        print()
    elif choice == "2":
        os.system('cls||clear')
        x = input("Enter Recipe Name: ")
    else:
        print("Invalid choice")


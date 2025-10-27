import helper
import hashmod
"""
1=> Register
2=> Login

Register: Username/email and password => Store the hash with the username
Login: username/email and password => Search through the text file and compare password

Database:
username:password_hash
"""

choices = [1,2]
choice = 0
while(choice not in choices):
    helper.display_main_menu()
    choice = int(input("Choice: "))

if (choice == 1):
    username = input("Username/Email: ")
    password = input("Password: ")
    byte_value = hashmod.to_byte(password)
    password_hash = hashmod.calculate_sha256(byte_value)
    helper.save_to_database(username,password_hash)
    print("Calculated successfully!!!")

elif (choice == 2):
    username = input("Username/Email: ")
    password = input("Password: ")
    existing_users = helper.load_users_from_database()
    if username not in existing_users:
        print("User does not exist, please register...")
        exit()
    hash_byte = hashmod.to_byte(password)
    hash_password = hashmod.calculate_sha256(hash_byte)
    if existing_users[username] == hash_password:
        print(f"Welcome back {username}!!!")
    else:
        print("Passowrd incorrect!!!")
        exit()
else:
    print("Invalid Option...")
    exit()
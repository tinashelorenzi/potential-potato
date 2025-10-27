
def save_to_database(username,password_hash):
    with open('database.txt','a') as file:
        file.write(f'{username}:{password_hash}\n')

def display_main_menu():
    print("""
==============================================================================================
          Fort Knocks Login System
==============================================================================================
          1 => Register to Fort knocks
          2 => Login to the Fortress of solitude
""")


def load_users_from_database():
    users = {}
    with open('database.txt','r') as file:
        for line in file:
            line = line.strip() #Separate from all other lines
            username,hash_password = line.split(':',1)
            users[username] = hash_password

            """
            {tinashe@powerpuffgirls:dfjdjfbsajdnsojDNSOJNSOID,}
            """
    
    return users
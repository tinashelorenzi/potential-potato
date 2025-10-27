from datetime import datetime,timedelta,timezone
class Pet:
    def __init__(self,name,gender,age,chip_number):
        self.name = name
        self.type = type
        self.gender = gender
        self.age = age
        self.chip_number = chip_number
        self.date_registered = datetime.now(timezone(timedelta(hours=2)))
        print("Pet Created Successfully!")
    
    #Methods
    def introduce(self):
        print(f"Hi bro! My name is {self.name}, and I am a {self.type}")
    
    #Modifiers -> method tto change attributes
    def transfer_chip(self,new_chipNumber):
        self.chip_number = new_chipNumber
        print("Transfer of pet pet successfully")
    
    def birthday(self):
        self.age += 1
        print("Happy what what to you...")

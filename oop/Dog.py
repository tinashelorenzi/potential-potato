from Pet import Pet
class Dog(Pet):
    def __init__(self,breed,awesome_level,name,age,gender,chip_number):
        #Inherit values from the parent Pet class!
        super().__init__(name,gender,age,chip_number)
        self.breed = breed
        self.awesome_less = awesome_level
    
    def introduce(self):
        print("Blah Blah Blah")
    
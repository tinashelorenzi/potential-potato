from Pet import Pet
class Cat(Pet):
    def __init__(self,color,paw_size,name,age,chip_number,gender):
        super().__init__(name,gender,age,chip_number)
        self.color = color
        self.paw_size = paw_size
    
    ########
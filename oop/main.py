from Pet import Pet
from Dog import Dog
from Cat import Cat

pet1 = Pet("Rolo","Dog","Male",17,"#3298u8e9")
print(pet1.name)
pet1.introduce()
print(pet1.chip_number)

pet1.transfer_chip("#938y49wrhw98y23")
print(pet1.chip_number)

dg1 = Dog("Bull Terrier",100,"Rolo",17,"Male","#9238ru839eu19e")
dg1.introduce()
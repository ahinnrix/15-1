#Header=========================================================================

#Amanda Hinnerichs
#Date: 04/16/2024
#Assignment cat.py
#Description: making a cat class

# Functions=====================================================================
class Cat:
    def __init__(self,name,sound,age,color):
        self.name = name
        self.sound = sound
        self.age = age
        self.color = color



#================================================================================

# Main===========================================================================
my_cat = Cat('Midnight', 'prrrrrrrr', 4, 'black')
print(my_cat.name)
print(my_cat.sound)
print(my_cat.age)
print(my_cat.color)




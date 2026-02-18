#48,49  Classes and Objects
# Class is the blueprint that create objects
# Attributes = Variables
# Behaviour = Methods
class Computer:

   def config(self):
       print("i5, 16GB, 1TB")

comp1 = Computer()
comp2 = Computer()

comp1.config()
#or
Computer.config(comp2)

from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


kai = Vehiculo("Negro", "4")
print(kai)

file = open('vehiculo_objeto', 'w+b')

dump(kai, file)

file.seek(0)
nuevo_kai = load(file)

print(nuevo_kai)
file.close()
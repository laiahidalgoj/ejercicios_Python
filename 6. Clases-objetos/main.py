class Vehicle():

    color = 'Black'
    wheels = 4
    doors = 4

class Car(Vehicle):
    speed = 80
    displacement = 50

audiQ7 = Car()
print('Speed: ', audiQ7.speed)
print('Displacement: ', audiQ7.displacement)
print('Color: ', audiQ7.color)
print('Wheels: ', audiQ7.wheels)
print('Doors: ', audiQ7.doors)

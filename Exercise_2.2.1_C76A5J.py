import math


#1.1. The volume of a sphere if radius is (4/3)*pi*r^3. The volume of a sphere if radius is 5

def sphere_volume(radius):
    volume = (4/3) * math.pi * math.pow(radius, 3)
    return volume

radius = 5

volume = sphere_volume(radius)

print(f"The volume of the sphere with {radius} is {volume: .2f} cubic units")







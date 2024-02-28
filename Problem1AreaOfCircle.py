import math

def areaOfCircle(r):

    area = (r**2) * math.pi
    
    return area

r = float(input("Enter radius of the circle: "))

print(areaOfCircle(r))


#Victor Moreno
#2/27/24

#Write a function 'areaOfCircle(r)' which returns the area of a circle of radius r.

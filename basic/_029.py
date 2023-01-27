#Invert colors
#Create a function that inverts the rgb values of a given tuple.

def invert_color(r, g, b):
    new_red = 255 - r
    new_green = 255 - g
    new_blue = 255 - b

    return (new_red, new_green, new_blue)


#print(invert_color(165, 180, 17))
red = int(input("RED: "))
green = int(input("GREEN: "))
blue = int(input("BLUE: "))

output = invert_color(red, green, blue)
print(f"The color {red, green, blue} inverted is: {output}")
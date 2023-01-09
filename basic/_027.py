# sum of resistance in series circuits


values = input("Enter the values separated by space: ").split()

array_values = []
for i in values:
    try:
        array_values.append(float(i))
    except ValueError:
        print("Error, the values is not numbers")


def series_resistance(arr):
    sum = 0
    for i in array_values:
        sum = sum + i
    
    return sum


print(f"{series_resistance(array_values)} ohms")



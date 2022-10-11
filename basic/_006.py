#Program to print natural numbers from 1 to N.

number = int(input("Enter a number: "))
i = 1

print("Natural numbers from 1 to {} are:".format(number))
while i <= number:
    print(i, end=" ")
    i += 1

print(" ")


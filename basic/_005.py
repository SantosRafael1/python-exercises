#Program to find the largest of two numbers
number1 = float(input("Enter 1° value: "))
number2 = float(input("Enter 2° value: "))

if (number1 > number2):
    print("{} is greatest.".format(number1))
    print("The first value win!")
elif(number2 > number1):
    print("{} is greatest.".format(number2))
    print("The second value win!")
else:
    print("{} and {} is equal!".format(number1, number2))
    print("Are they twins?")




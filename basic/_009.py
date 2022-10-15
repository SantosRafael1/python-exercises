#Program to print odd numbers from 0 to 100

user_number = int(input("Enter a number: "))

while( user_number < 100 ):
    if( user_number % 2 != 0 ):
        print(user_number)
    user_number = user_number + 1



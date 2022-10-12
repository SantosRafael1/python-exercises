#Program to check if a year is leap or not

while(True):

    year = int(input("Enter the year (Press 0 to exit): "))

    if(year == 0):
        break

    if (year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                print(f"{year} IS a leap year.")
            else:
                print(f"{year} is NOT a leap year.")
        else:
            print(f"{year} IS a leap year")
    else:
        print(f"{year} is NOT a leap year")


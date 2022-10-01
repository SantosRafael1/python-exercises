#Enter two numbers and perform all arithmetic operations
print("Enter two numbers:")
n1, n2 = int(input()), int(input())

print(f"Sum: {n1} + {n2} = {n1+n2}")
print(f"Difference: {n1} - {n2} = {n1-n2}")
print(f"Product: {n1} x {n2} = {n1*n2}")
print(f"Quotient: {n1} / {n2} = {round(n1/n2, 2)}")
print(f"Modulos: {n1} % {n2} = {n1%n2}")

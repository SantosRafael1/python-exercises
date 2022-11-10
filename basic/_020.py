#Gasto de combustivel

time = int(input("Tempo gasto na viagem: "))
speed = int(input("Velocidade média: "))

fuel_consumption = (time * speed) / 12
print("%.3f" % fuel_consumption)
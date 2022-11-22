#Conversão de tempo

n = int(input())

hour = n / 3600
minute = (hour * 60) % 60
seconds = (hour * 3600) % 60

print(f"{int(hour)}:{int(minute)}:{int(seconds)}")
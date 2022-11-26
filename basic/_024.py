# Idade em dias

days = int(input("Age in days: "))

years = int(days / 365)
days -= years * 365

months = int(days / 30)
days -= months * 30

print(f"{years} ano(s)")
print(f"{months} mese(s)")
print(f"{days} dia(s)")

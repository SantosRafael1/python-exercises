#cédulas

amount = int(input())

print(amount)
print("{} nota(s) de R$ 100,00".format(int(amount/100)))
note = (amount%100)
print("{} nota(s) de R$ 50,00".format(int(note/50)))
note = (note%50)
print("{} nota(s) de R$ 20,00".format(int(note/20)))
note= (note%20)
print("{} nota(s) de R$ 10,00".format(int(note/10)))
note = (note%10)
print("{} nota(s) de R$ 5,00".format(int(note/5)))
note= (note%5)
print("{} nota(s) de R$ 2,00".format(int(note/2)))
note = (note%2)
print("{} nota(s) de R$ 1,00".format(int(note/1)))
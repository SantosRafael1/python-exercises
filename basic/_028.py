# find discount

def find_discount(price, discount):
    dis = price * (discount / 100)
    final_price = price - dis
    return final_price


print(find_discount(1500, 50))
print(find_discount(89, 20))
print(find_discount(211, 50))
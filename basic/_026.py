# Curzon number

num = int(input("Check whether is a curzon or not: "))

def is_curzon(n):
    f_value = 2 * n + 1
    s_value = pow(2, n) + 1
    condition = s_value % f_value == 0
    if condition:
        #The print statements are just to see the value of operation
        #print(f_value % s_value)
        return True
    else:
        #The print statements are just to see the value of operation
        #print(f_value % s_value)
        return False


print(is_curzon(num))

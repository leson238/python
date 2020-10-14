# Multiply a and b without the help of multiply sign
def russian_peasant(a,b):
    result = 0
    while b > 0:
        # If b is odd increase result by a
        if b & 1:
            result += a 
        # Multiply a and divide b by 2
        a = a << 1
        b = b >> 1            
    return result

print(russian_peasant(4,4))


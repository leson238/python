# Ask for input integer n, loop infinite until get right format
while (True):
    n = input("Please input n: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Wrong format. Please input an integer!")
# Copy n to another variable, for output readability
copy_n = n
# Initiate result r as an empty string
r = ''
while n > 0:
    # Repeat the process for each Roman numeral equivalent, from high to low
    if n >= 900:
        c = n // 900    # Integer divident, to find the highest value v less than or equal n
        r += c * "CM"   # Append Roman numeral equivalent to the result r
        n -= c * 900    # Deduct value v from n
    elif n >= 500:
        c = n // 500
        r += c * "D"
        n -= c * 500
    elif n >= 400:
        c = n // 400
        r += c * "CD"
        n -= c * 400
    elif n >= 100:
        c = n // 100
        r += c * "C"
        n -= c * 100
    elif n >= 90:
        c = n // 90
        r += c * "XC"
        n -= c * 90
    elif n >= 50:
        c = n // 50
        r += c * "L"
        n -= c * 50
    elif n >= 40:
        c = n // 40
        r += c * "XL"
        n -= c * 40
    elif n >= 10:
        c = n // 10
        r += c * "X"
        n -= c * 10
    elif n >= 9:
        c = n // 9
        r += c * "IX"
        n -= c * 9
    elif n >= 5:
        c = n // 5
        r += c * "V"
        n -= c * 5
    elif n >= 4:
        c = n // 4
        r += c * "IV"
        n -= 4
    else:
        c = n
        r += c * "I"
        n -= c
# Print the result


# Much more elegant, just function and global vars
# def convert(s, num):
#     global n, r
#     c = n // num
#     r += s * c
#     n -= c * num


# convert("CM", 900)
# convert("D", 500)
# convert("CD", 400)
# convert("C", 100)
# convert("XC", 90)
# convert("L", 50)
# convert("XL", 40)
# convert("X", 10)
# convert("IX", 9)
# convert("V", 5)
# convert("IV", 4)
# convert("I", 1)

print(f"The Roman numeral version of {copy_n} is {r}")

s = '\t\t\ta\t\t\tn'
s = s.replace("\t", '')
print(s)

#Convert Binary to Decimal--------------------------------
def binarytoDec(binary_num):
    str_num = str(binary_num)
    length = len(str_num)
    decimal = 0
    for i in range(length):
        digit = int(str_num[i])  # Convert character to integer
        power = length - 1 - i   # Correct power of 2 for this position
        decimal += digit * (2 ** power)
    return decimal

print(binarytoDec(1011))  # Output: 11

#Convert Binary to Decimal--------------------------------
# def binarytoDec(binary_num):
#     str_num = str(binary_num)
#     length = len(str_num)
#     decimal = 0
#     for i in range(length):
#         digit = int(str_num[i])  # Convert character to integer
#         power = length - 1 - i   # Correct power of 2 for this position
#         decimal += digit * (2 ** power)
#     return decimal

# print(binarytoDec(1011))  # Output: 11


# Binary to decimal---------------
# 11 ÷ 2 = 5 remainder 1
#  5 ÷ 2 = 2 remainder 1
#  2 ÷ 2 = 1 remainder 0
#  1 ÷ 2 = 0 remainder 1


# def decimal_to_binary(n):
#     binary=""
#     while n>0:
#         remainder=n%2
#         binary=str(remainder)+binary
#         n=n//2
#     return binary if binary else "0"
    
    
# print(decimal_to_binary(11))  # Output: '10



# Convert Decimal to Octal --------------------------------------
# def des_octal(decimal):
#     if decimal==0:
#         return "0"
#     octal=""
#     while decimal>0:
#         remainder=str(decimal%8)
#         octal=remainder+octal
#         decimal//=8
#     return octal
    
# decimal=38
# print(des_octal(decimal))


#Octal to Decimal Conversion----------------------------
def octToDec(oct):
    if oct==0:
        return "0"
    dec=0
    stroct=str(oct)
    for i in range(len(str(oct))):
        digit=int(stroct[i])
        power=len(stroct)-1-i
        dec=dec+digit*(8**power)
    return dec

oct=345
print(octToDec(oct))

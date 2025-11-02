#Check if a number is Palindrome or Not-----------------

# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         digit=num%10  #it give last digit  - remainder
#         rev=rev*10+digit
#         num//10
#     return temp==rev


# num=45549
# if palindrome(num):
#     print("Palindrome")
# else:
#     print("Not palindrome")


# Find all Palindrome Numbers in a given range-----------------------

# def palindrome(num):
#     temp = num
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     return temp == rev

# start = 10
# end = 50
# palindr = []

# for num in range(start, end + 1):
#     if palindrome(num):
#         palindr.append(num)

# print(palindr)
   
#Check if a number is prime or not-----------------------

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=4
if prime(num):
    print("Prime")
else:
    print("Not prime")


#Prime Numbers in a given range----------------------

a = 10
b = 16
prime_num=[]
for i in range(a, b+1):
    
    if prime(i):
        prime_num.append(i)
print(prime_num)

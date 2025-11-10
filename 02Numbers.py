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

# def prime(num):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# num=4
# if prime(num):
#     print("Prime")
# else:
#     print("Not prime")


#Prime Numbers in a given range----------------------

# a = 10
# b = 16
# prime_num=[]
# for i in range(a, b+1):
    
#     if prime(i):
#         prime_num.append(i)
# print(prime_num)

   
#Check if a number is Armstrong Number or not--------------------
# def is_armstrong(num):
#     n = len(str(num))
#     total = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** n
#         temp //= 10
#     return total == num

# num = 153
# if is_armstrong(num):
#     print("Armstrong")
# else:
#     print("Not Armstrong")


#Check whether a number is Perfect Number or not-------------------------
# def perfectNum(num):
#     if num<=1:
#         return False
#     sum=0
#     for i in range(1, num):
#         if num%i==0:
#             sum=sum+i
#     return sum==num

# num=22
# if perfectNum(num):
#     print("Perfect")
# else:
#     print("Not perfect")

  
#Check whether a given number is even or odd-------------------
# def oddEven(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# num=0
# oddEven(num) 

#Sum of first N Natural Numbers-----------
# def sumofNum(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     return sum

# num=6
# print(sumofNum(num))

#Find Sum of AP Series---------------------

# def ap(a, d,n):
#     sum_ap=(n/2)*(2*a+(n-1)*d)
#     return int(sum_ap)

# print("Sum of a ", ap(2,2,4))

#Check a A.P series---------------------

# def ap_series(series):
#     if len(series)<2:
#         return False
#     d=series[1]-series[0] # common diff

#     for i in range(1, len(series)-1):
#         if series[i+1]-series[i]!=d:
#             return False
#     return True

# series = [2, 4, 6, 8]
# print("Series is A.P.?" , ap_series(series))  # True


#Program to find Sum of GP Series------------
# def sum_GP(a, r, n): #r=common ratio, a=first term, n=num of terms
#     if r==1:
#         return a*n
#     else:
#         return a*(1-r**n)/(1-r)
# a=float(input("Enter a"))
# n=float(input("Enter n"))
# r=float(input("Enter r"))

# print(sum_GP(a,r,n))

#program to find a Gp series--------------
# def isGP(series):
#     r=series[1]/series[0]
#     for i in range(1, len(series)-1):
#         if series[i+1]/series[i]!=r:
#             return False
#     return True


# series=[2,4,8,16]
# print(isGP(series))

#Greatest of 3 numbers----------------------

# def greatest(a,b,c):
#     if a>b and a >c:
#         print(a, "is greatest")
#     elif b>a and b>c:
#         print(b, "is greatest")
#     else:
#         print(c, "is greatest")
# greatest(34,322,1234)

#Check if given year is a leap year or not-------------------------

# def is_leap_year(year):
#     if (year % 4 == 0):
#         if (year % 100 != 0) or (year % 400 == 0):
#             return "Yes"
#     return "No"

# # Example usage
# year = int(input("Enter a year: "))
# print(is_leap_year(year))
 

#Reverse digits of a number---------
# def revrse_Num(num):
#     rev=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         rev=rev*10+digit

#         temp//=10
#     return rev



# num=654
# print(revrse_Num(num))


#Maximum and Minimum Digit in a Number------------------

# def min_max(num):
#     min_digit = 9
#     max_digit = 0
#     while num>0:
#         digit=num%10
#         if digit < min_digit:
#             min_digit = digit
#         if digit > max_digit:
#             max_digit = digit
#         num=num//10
#     return min_digit, max_digit
# num=2746
# min_d, max_d=min_max(num)
# print("Minimum Digit:", min_d)
# print("Maximum Digit:", max_d)


#Print Fibonacci Series up to Nth term--------------------
# def fibo(n):
#     fib=[0,1]
#     new_term=0
#     for i in range(1,n-1):
#         new_term=fib[i]+fib[i-1]
#         fib.append(new_term)
#     return fib

# n=6
# print(fibo(n))

#Factorial of a Number : Iterative and Recursive----------------------

#iterative

# def fact(num):
#     facti=1
#     for i in range(num, 0, -1):
#         facti=i*facti
#     return facti

#recursive
# def fact(num):
#     if num==1 or num==0:
#         return 1
#     return num*fact(num-1)
# num=8
# print(fact(num))


#Calculate the Power of a Number------------

# def power(num, pow):
#     return num**pow
# print(power(2,4))

# #Factors of a Given Number-------------------
# def factors(num):
#     fcators_lst=[]
#     for i in range(1, num+1):
#         if num%i==0:
#             fcators_lst.append(i)
#     return fcators_lst
# print(factors(9))


#Print all Prime Factors of the given number--------------------
# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2, n):
#         if n%i==0:
#             return False
#     return True
# def primFactors(num):

#     prime_fact=[]
#     for i in range(1, num+1):
#         if num%i==0 and prime(i):
#             prime_fact.append(i)
#     return prime_fact
# print(primFactors(52))

#Check if a number is a Strong Number or not----------------
#perfect num= 145=1!+4!+5!

# def fact(x):
#     if x==0 or x==1:
#         return 1
#     return x*fact(x-1)
# def strongNum(num):
#     temp=num
#     sum=0
#     while num>0:
#         digit=num%10
#         sum=sum+fact(digit)
#         num=num//10
#     return sum==temp
    
# num=26
# if strongNum(num):
#     print("Strong Num")
# else:
#     print("Not strong")

#Check if a number is Automorphic Number--------------
#Input Format: N = 76
#Result: Automorphic Number
#Explanation: Calculating 76 * 76 gives 5776, it ends with the given number

def automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

num=76
if automorphic(num):
    print("Automorphic Num")
else:
    print("Not automorphic num")


#Find GCD of two numbers-----------------------------------

def gcd(a, b):
    while b!=0:
        a,b= b, a%b
    return a
    
a=26
b=12
print(gcd(a,b))


# lcm-----------------------------------------------

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Example usage
a = 8
b = 4

print("LCM of", a, "and", b, "is:", lcm(a, b))


#Check if the given number is Harshad(Or Niven) Number-------------------------------------
#3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

def harshadNum(num):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit
        temp=temp//10
        
    return num%sum==0
num=378
if harshadNum(num):
    print("Harshad num")
else:
    print("Not harshad num")

    

    

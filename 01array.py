# find smallest number----------------
# arr = [2, 5, 1, 3, 0, -29, 45]
# small = arr[0]
# for i in range(1, len(arr)):
#     if arr[i] < small:
#         small = arr[i]
# print(small)


#find the largest number-------
# arr=[2,5,13,3,100]
# def large(arr):
#     largest=max(arr)
#     for i in range(0, len(arr)):
#         if largest<arr[i]:
#             largest=arr[i]
#     return largest
# print(large(arr))


#find second smallest and second largest num in array
# arr=[2,5,13,3,100]
# def large(arr):
#     largest=max(arr)
#     for i in range(0, len(arr)):
#         if largest<arr[i]:
#             largest=arr[i]
#     return largest

# def smallest(arr):
#     small=arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] < small:
#             small = arr[i]
#     return small

# def secondlarge(arr):
#     # second = float('-inf')
#     second=min(arr)
#     for i in range(0, len(arr)):
#         if second<arr[i] and large(arr)!=arr[i]:
#             second=arr[i]
#     return second

# def secondsmallest(arr):
#     second = float('inf') 
#     for i in range(1, len(arr)):
#         if arr[i] < second and arr[i]!=smallest(arr):
#             second = arr[i]
#     return second
# print(f" second smallest {secondsmallest(arr)} and second largest {secondlarge(arr)}") 


#reverse an array-----------------
# arr=[5,4,3,2,1]
# def reverse(arr):
#     newarr=[]
#     for i in range(len(arr)-1,-1,-1):
#         newarr.append(arr[i])
#     return newarr
# print(reverse(arr))

#count the frequency of each element in an array-----------------
# arr=[10,5,10,15,10,15]
# def frequencycount(arr):
#     freq={}
#     for i in arr:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# print(frequencycount(arr))
            

# rearrange the array in increasing and decreasing order--------------
# arr=[8, 7, 1, 6, 5, 9]
# def inc_dec(arr):
#     arr.sort()
#     half=len(arr)//2
#     arr[half:]=arr[half:][::-1]
#     print(arr)

# inc_dec(arr)

#calculate sum of elements in array
# array=[1,2,3,4,5,5]
# sum=0
# for el in array:
#     sum=sum+el
# print(sum)

#rotate the array right by K -----------------
# arr=[1,2,3,4,5]
# def rorate_right(arr,k):
#     n=len(arr)
#     k=k%n #in case k >array length
#     return arr[-k:]+arr[:-k]
# k=2
# rottedarr=rorate_right(arr,k)
# print(rottedarr)


#rotate the array left by K ---------------

# def leftRotate(arr, k):
#     n=len(arr)
#     k=k%n
#     return arr[k:]+arr[:k]

# arr=[1,2,53,6,74,5,78,90]
# k=2
# print(leftRotate(arr,k))


#avgerage of all elments in array

# arr=[1,2,1,1,5,1]
# sum=0
# for el in arr:
#     sum=sum+el
# avg=round(sum/len(arr),2)

# print(avg)

#find median in array-middle ele after sorting------------------
# arr=[2,5,1,7]
# def median(arr):    
#     arr.sort()
#     n=len(arr)
#     middle=len(arr)//2
#     if n%2!=0: #odd
#         return arr[middle]
#     else:  #even
#         return (arr[middle]+arr[middle-1])/2
    
# print(median(arr))

# remove duplicate from sorted array-----------------

# arr=[1,2,3,1,2,3,3,3,1,1,4,4,4,55,5,5,1,34,34]
# def remove_dup(arr):
#     arr.sort()
#     new_arr=[]
#     for el in arr:
#         if el in new_arr:
#             continue
#         else:
#             new_arr.append(el)
#     return new_arr

# print(remove_dup(arr))

# #---------------------  new method
# arr.sort()
# new_arr = sorted(set(arr))


#adding an element in arr------------------------
# arr=[1,2,3,4,5]

# def insertBegin(val):
#     global arr
#     arr=[val]+arr  #new list
#     print(arr)

# def insertLast(val):
#     global arr
#     arr=arr+[val]
#     print(arr)
# def insertatPos(pos,val):
#     global arr
#     arr=arr[:pos]+[val]+arr[pos:]
#     print(arr)

# insertBegin(10)
# insertLast(20)
# insertatPos(3, 15) 


# Find repeating elements in array-----------------------------

# arr= [1,1,2,3,4,4,5,2,8,8]
# def repeating(arr):
#     arr.sort()
#     repeatingArr=[]
#     for i in range(0,len(arr)-1):
#         if arr[i]==arr[i+1] and arr[i] not in repeatingArr:
#             repeatingArr.append(arr[i])
#         else:
#             continue
#     return repeatingArr
# print(repeating(arr))

# Find non repeating elements in array-----------------------------
# arr= [1,1,2,3,4,4,5,2,8,8,22]
# def nonrepeating(arr):
#     freq={}
#     for el in arr:
#         if el not in freq:
#             freq[el]=1
#         else:
#             freq[el]=freq[el]+1
#     non_repeat=[]
#     for key in freq:
#         if freq[key]==1:
#             non_repeat.append(key)
#     return non_repeat

    
# print(nonrepeating(arr))



















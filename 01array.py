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

#find all symmetric pairs in an array -------------------

# def find_symmetric(pairs):
#     seen={}
#     symmetric=[]
#     for (a,b) in pairs:
#         if (b,a) in seen:
#             symmetric.append((a,b))
#         else:
#             seen[(a,b)]=True  #add a,b in seen
#     return symmetric


# pairs=[(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
# print(find_symmetric(pairs))


# Maximum Product Subarray in an Array----------------------
# def maxProduct(nums):
#     # Initialize variables
#     max_prod = nums[0]
#     min_prod = nums[0]
#     result = nums[0]
    
#     # Traverse from 1st index
#     for i in range(1, len(nums)):
#         # If current number is negative, swap max and min
#         if nums[i] < 0:
#             max_prod, min_prod = min_prod, max_prod
        
#         # Update max and min products
#         max_prod = max(nums[i], max_prod * nums[i])
#         min_prod = min(nums[i], min_prod * nums[i])
        
#         # Update final result
#         result = max(result, max_prod)
    
#     return result

# # Example 1
# nums1 = [1, 2, 3, 4, 5, 0]
# print(maxProduct(nums1))  # Output: 120

# # Example 2
# nums2 = [1, 2, -3, 0, -4, -5]
# print(maxProduct(nums2))  # Output: 20


#Replace elements by its rank in the array--------------------

# def rank(arr):
#     sorted_arr=sorted(arr)
#     rank_dict={}
#     rank=1

#     for num in sorted_arr:
#         if num not in rank_dict:
#             rank_dict[num]=rank
#             rank=rank+1
#     #replace elements in original array with rank
#     ans=[]
#     for num in arr:
#         ans.append(rank_dict[num])
#     return ans

         
# arr=[20, 15, 26, 2 ,98, 6]
# print(rank(arr))

#Sort Elements of an Array by Frequency----------
# def sortFreq(arr):
#     freq={}
#     visit=[]
   
#     for el in arr:
#         if el not in visit:
#             freq[el]=1
#             visit.append(el)
#         else:
#             freq[el]=freq[el]+1

#     sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

# # freq.items()	Turns dictionary into list of (key, value) pairs
# # lambda x: x[1]	Sort using the value (frequency)
# # reverse=True	Sort from high to low
# # dict(...)	Converts sorted list back into a dictionary
    
#     return freq

# arr=[1,2,3,2,4,3,1,2]
# print(sortFreq(arr))


# Rotate arrayby k elements-------------------------
# arr=[1,2,3,4,5,6,7]
# def rotate(arr, k):
#     n=len(arr)
#     k=k%n
#     return arr[-k:]+arr[:-k]

# k=3
# print(rotate(arr, k))


#An equilibrium index in an array is a position where the sum of all elements to its left is equal to the sum of all elements to its right.------------

# def equilibrium(arr):
#     total_sum=sum(arr)
#     left_sum=0
#     for i in range(len(arr)):
#         if left_sum==total_sum-arr[i]-left_sum:
#             return i
#         left_sum+=arr[i]
#     return -1
            

# arr=[2, 3, -1, 8, 4]
# print(equilibrium(arr))


#Linear Search-------------------
# arr=[1,2,3,5,2,2,1]
# key=3
# def search(arr, key):
#     for i in range(len(arr)):
#         if arr[i]==key:
#             return i
#     return -1
        
# print(search(arr, key))

#Check if array is subset of another array------------------
# def subset(arr1, arr2):
    
#     if len(arr2)>len(arr1) or len(arr2)==0:
#         return False
#     for el in arr2:
#         if el not in arr1:
#             return False
#     return True
    
       
# arr1= [1,3,4,5,2]
# arr2= [2,3]

# if subset(arr1, arr2):
#     print("arr2 is subset of arr 1")
# else:
#     print("arr2 is not subset of arr1")

    

  
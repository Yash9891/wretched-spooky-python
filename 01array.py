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
arr=[10,5,10,15,10,15]
def frequencycount(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
print(frequencycount(arr))
            








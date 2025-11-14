#linear Search------------------------------
# def linearSearch(arr,target):
#     for i in range(len(arr)):
#         if target==arr[i]:
#             return i
#     return -1
    

# arr=[23,54,12,78,12,50,2]
# ans=linearSearch(arr,239)
# if ans==-1:
#     print("Not present")
# else:
#     print(f"Element is present at index {ans}")


#Binary Search----------------------------

# def binarySearch(arr, target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2

#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1


# arr=[4,5,6,7,8,89,90]
# # arr.sort()
# result=binarySearch(arr, 89)
# if result != -1:
#     print("Found at index:", result)
# else:
#     print("Not found")

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



# Bubble sort algorithm--------------------------------
#Bubble sort compares neighboring elements and swaps them if they are in the wrong order.

# def bubbleSort(arr):

#     n=len(arr)
#     for i in range(n):
#         for j in range(0, n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr

# arr = [13, 46, 24, 52, 20, 9]
# print(bubbleSort(arr))


#Selection sort---------------------------------------------
#Selection sort works by repeatedly selecting the smallest element from the unsorted part of the array and putting it in its correct position in the sorted part.

# def selectionSort(arr):

#     for i in range(len(arr)):
#         min_index=i # assume current index has the minimum
#         for j in range(i+1,len(arr)):
#             if arr[min_index]>arr[j]:
#                 min_index=j
#          # swap the found minimum element with element at i
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr

# arr=[9, 46, 24, 52, 20, 13]
# print(selectionSort(arr))


#Insertion sort--------------------------------------------------
#Insertion Sort is a simple and intuitive sorting algorithm that works the same way you arrange cards in your hand.

def insertionSort(arr):
    n=len(arr)

    for i in range(1, n):
        key=arr[i]   # element to be inserted
        j=i-1

        # Move elements greater than key to one position ahead
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1] = key   # place the key in correct position

    return arr
           
arr = [13, 46, 24, 52, 20, 9]
print(insertionSort(arr))
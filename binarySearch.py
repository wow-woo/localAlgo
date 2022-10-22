# Let's implement Binary Search
# n is number of items in array.
# target is the number you are looking for.
# Check if the number exists in the array.
n = 10
target = 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
# Recursive method


def BinarySearch(arr, start_idx, end_idx, target):
    if start_idx > end_idx:
        return None

    mid_idx = (end_idx + start_idx) // 2

    if target == arr[mid_idx]:
        return mid_idx
    elif target > arr[mid_idx]:
        return BinarySearch(arr, mid_idx+1, end_idx, target)
    elif target < arr[mid_idx]:
        return BinarySearch(arr, start_idx, mid_idx-1, target)


result = BinarySearch(arr, 0, n-1, target)
result2 = BinarySearch(arr2, 0, n-1, target)
if result:
    print(f"{target} is positioned in {result+1}th place")
else:
    print("Not Exists")
if result2:
    print(f"{target} is positioned in {result2+1}th place")
else:
    print("Not Exists")

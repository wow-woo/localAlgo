# This time i'm going to implement while loop Binary Search
# n is number of items in array.
# target is the number you are looking for.
# Check if the number exists in the array.
n = 10
target = 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]


def binary_search_loop(arr, target, n):
    start_inx = 0
    end_idx = n-1

    while start_inx <= end_idx:
        mid_idx = (start_inx+end_idx) // 2

        if target == arr[mid_idx]:
            return mid_idx
        elif target > arr[mid_idx]:
            start_inx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    return None


result = binary_search_loop(arr, target, n)
result2 = binary_search_loop(arr2, target, n)
if result:
    print(f"{target} is positioned in {result+1}th place.")
else:
    print("Not Exists")
if result2:
    print(f"{target} is positioned in {result2+1}th place.")
else:
    print("Not Exists")

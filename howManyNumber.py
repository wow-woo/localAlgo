# how many times x are in array?
# implement this with O(logN)
from bisect import bisect_left, bisect_right
from turtle import left

arr = [1, 1, 2, 2, 2, 2, 3]
x = 2


def count_how_many_number(arr, target_number):
    left_idx = bisect_left(arr, target_number)
    right_idx = bisect_right(arr, target_number)
    return right_idx-left_idx


result = count_how_many_number(arr, x)
# returns -1, if x is absent.
if result <= 0:
    print(-1)
else:
    print('Number', x, "exists", result, 'once/times in array')

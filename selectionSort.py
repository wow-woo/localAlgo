# select right data to be in right position.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(arr):
    len_numbers = len(arr)
    for target_idx in range(0, len_numbers):
        target_number = arr[target_idx]
        replacement = target_number
        replacement_idx = target_idx
        for current_idx in range(target_idx+1, len_numbers):
            current_number = arr[current_idx]
            if current_number < replacement:
                replacement = current_number
                replacement_idx = current_idx
        if replacement < target_number:
            arr[replacement_idx] = target_number
            arr[target_idx] = replacement
    return arr


print(selection_sort(arr))

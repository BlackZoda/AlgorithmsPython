
from algorithms.time_complexity import (
    constant_time_lookup,
    linear_search,
    bubble_sort,
    binary_search,
    merge_sort)

sorted_arr = [1, 2, 3, 4, 5]

print(constant_time_lookup(sorted_arr, 3))

print(linear_search(sorted_arr, 3))

unsorted_arr = [5, 2, 4, 3, 1]

print(bubble_sort(unsorted_arr))

print(binary_search(unsorted_arr, 3))

merge_sorted_array = merge_sort(unsorted_arr)

print(merge_sorted_array)

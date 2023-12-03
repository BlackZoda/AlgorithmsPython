# Constant Time - O(1)
def constant_time_lookup(arr, index):
    return arr[index]


# Linear Time - O(n)
def linear_search(lst, needle):
    for element in lst:
        if element == needle:
            return True
    return False


# Quadratic Time - O(n^2)
def bubble_sort(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


# Logarithmic Time - O(log n)
def binary_search(lst, needle):
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2
        mid_value = lst[mid]

        if mid_value == needle:
            return mid
        elif mid_value < needle:
            low = mid + 1
        else:
            high = mid

    return -1


# Combination of Linear and Logarithmic time - O(n log n)
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    return result + left[left_index:] + right[right_index:]

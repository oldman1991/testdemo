# coding=utf-8
# create by oldman at 2018/5/21
"""
快速排序
"""


# def quicksort(array, left, right):
#     if left >= right:
#         return array
#     low = left
#     high = right
#     key = array[left]
#     while left < right:
#         while left < right and array[right] >= key:
#             right -= 1
#         array[left] = array[right]
#         while left < right and array[left] <= key:
#             left += 1
#         array[right] = array[left]
#     array[left] = key
#
#     quicksort(array, low, left-1)
#     quicksort(array, left + 1, high)

# def quicksort(array, left, right):
#     if left>=right:
#         return array
#     low = left
#     high = right
#     key = array[left]
#     while left < right:
#         while left< right and array[right]>=key:
#             right-=1
#         array[left] = array[right]
#
#         while left< right and array[left]<=key:
#             left+=1
#         array[right] = array[left]
#
#     array[left] = key
#
#     quicksort(array, low, left-1)
#     quicksort(array, left+1, high)


def quick_sort(array, left, right):

    if left>=right:
        return
    low, high = left, right
    pivot = array[left]
    while left<right:
        while left< right and array[right]>=pivot:
            right -= 1
        array[left] = array[right]

        while left< right and array[left]<= pivot:
            left += 1
        array[right] = array[left]
    array[left] = pivot
    quick_sort(array, low, left-1)
    quick_sort(array, left+1, high)



a = [5, 4, 6, 8, 7, 9, 12, 11, 10, 0, 5]
quick_sort(a, 0, len(a) - 1)
print(a)

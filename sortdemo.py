# coding=utf-8


def insert_sort(para):
    """
    插入排序算法:
    时间复杂度为O(n^2)
    """
    count = 0
    for i in range(len(para)):
        min_index = i
        for j in range(i):
            count += 1
            if para[min_index] < para[j]:
                min_index = j
                tmp = para[i]
                para[i] = para[min_index]
                para[min_index] = tmp
    print(para)
    print(count)


para = [4, 1, 2, 3, 5, 7, 6, 4, 5, 4, 5, 9, 5]


# insert_sort(para)

def bubble_sort(param):
    """
    冒泡排序算法:
    时间复杂度为O(N^2)
    """
    count = 0
    for i in range(len(param)):
        for j in range(i + 1, len(param)):
            count += 1
            if param[i] > param[j]:
                temp = param[i]
                param[i] = param[j]
                param[j] = temp
    print(param)
    print(count)

bubble_sort(param=para)
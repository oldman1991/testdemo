# coding=utf-8
# create by oldman at 2018/3/19

def sift_down01(array, start, end):
    """
    调整成最大堆，初始堆时，从下往上；交换堆顶与堆尾后，从上往下调整
    :param array: 列表的引用
    :param start: 父节点
    :param end: 结束的下标
    :return: 无
    """
    # 当列表第一个是以下标0开始，节点下标为i，左孩子则为2i+1,有孩子则为2i+2;
    left_child = 2 * start + 1
    # 当节点的有孩子存在 且大于节点的左孩子时
    if left_child + 1 <= end and array[left_child + 1] > array[left_child]:
        left_child += 1
    if array[left_child] > array[start]:  # 当左右孩子的最大值大于父节点时，则交换
        tmp = array[left_child]
        array[left_child] = array[start]
        array[start] = tmp

    print(">>", array)


"""
上面的有一个问题，优化
"""


def sift_down02(array, start, end):
    while True:
        # 当列表第一个是以下标0开始，节点下标为i，左孩子则为2i+1,有孩子则为2i+2;
        left_child = 2 * start + 1
        # 当节点的有孩子存在 且大于节点的左孩子时
        if left_child + 1 <= end and array[left_child + 1] > array[left_child]:
            left_child += 1
        if array[left_child] > array[start]:  # 当左右孩子的最大值大于父节点时，则交换
            array[left_child], array[start] = array[start], array[left_child]
        else:  # 若父节点大于左右孩子，则退出循环
            break
        print(">>", array)


"""
继续优化，超出索引
"""


def sift_down(array, start, end):
    while True:
        # 当列表第一个是以下标0开始，节点下标为i，左孩子则为2i+1,有孩子则为2i+2;
        left_child = 2 * start + 1

        if left_child > end:
            break
        # 当节点的有孩子存在 且大于节点的左孩子时
        if left_child + 1 <= end and array[left_child + 1] > array[left_child]:
            left_child += 1
        if array[left_child] > array[start]:  # 当左右孩子的最大值大于父节点时，则交换
            tmp = array[left_child]
            array[left_child] = array[start]
            array[start] = tmp
            start = left_child
        else:  # 若父节点大于左右孩子，则退出循环
            break
        print(">>", array)


def heap_sort(array):  # 堆排序
    # 先初始化最大顶堆
    first = len(array) // 2 - 1  # 最后一个有孩子的节点(//表示取整的意思)
    for i in range(first, -1, -1):  # 从最后一个有孩子的节点开始往上去调整
        print(array[i])
        sift_down(array, i, len(array) - 1)
    print("初始化大顶堆的结果：", array)

    for head_end in range(len(array) - 1, 0, -1):
        array[head_end], array[0] = array[0], array[head_end]
        sift_down(array, 0, head_end - 1)  # 精髓就是首次调整为最大堆后，后面的调整会很方便。
        print(array)


if __name__ == "__main__":
    array = [16, 7, 3, 20, 17, 8]
    heap_sort(array)
    print(array)

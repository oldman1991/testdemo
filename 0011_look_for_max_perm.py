# coding=utf-8
# create by oldman at 2018/1/19
"""
寻找最大排列问题的递归算法思路的朴素实现方案
"""


def naive_max_perm(M, A=None):
    """
    在这个方法中，函数会接收到一个代表剩余人员的集合(A)，并创建一个代表被指向作为的集合(B),
    然后改函数会找出并删除集合A中某个不属于集合B的元素，再继续递归解决剩余人员的问题。
    :param M:
    :param A:
    :return:
    """
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1: return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


"""
寻找最大排列问题
"""


def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

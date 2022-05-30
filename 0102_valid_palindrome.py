# coding: utf-8
""" 
@author: oldman
@file: 0102_valid_palindrome.py 
@time: 2020-05-19 17:16
"""
"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def valid_palindrome(s: str) -> bool:
    def check_palindrome(low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1

    low, high = 0, len(s) - 1

    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return check_palindrome(low + 1, high) or check_palindrome(low, high - 1)

    return True


if __name__ == "__main__":
    s = "abc"
    s2 = "abcba"
    assert valid_palindrome(s) == False
    assert valid_palindrome(s2) == True

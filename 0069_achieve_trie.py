"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

"""
import unittest

class Trie:
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie
        :param word:
        :return:
        """
        children = self.root
        for char in word:
            if char not in children:
                children[char] = {}
            children = children[char]
        children["is_end"] = True

    def search(self, word: str) -> bool:
        """
        Return if the word is in the trie
        :param word:
        :return:
        """
        children = self.root
        for char in word:
            if char not in children:
                return False
            children = children[char]
        return children.get('is_end', False)

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that
        starts with the given prefis
        :param prefix:
        :return:
        """
        children = self.root
        for char in prefix:
            if char not in children:
                return False
            children = children[char]
        return False


class TestTrie(unittest.TestCase):
    def test_trie(self):
        obj = Trie()
        obj.insert("hello")
        self.assertEqual(obj.search("hello"), True)



unittest.main()

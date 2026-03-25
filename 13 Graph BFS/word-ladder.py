from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, length + 1))
                        visited.add(next_word)

        return 0

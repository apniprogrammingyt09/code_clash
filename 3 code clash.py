#You are given an array of integers arr of size n. A subarray of arr is defined as any contiguous segment of the array. A subarray is considered magical if:
from collections import deque

def diff(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return count == 1

def ladder_length(n, begin_word, end_word, word_list):
    word_list.sort()
    filtered_words = [word for i, word in enumerate(word_list) if i % 2 == 0]

    if end_word not in filtered_words:
        return 0

    queue = deque([(begin_word, 1)])
    visited = set()
    visited.add(begin_word)

    while queue:
        current_word, level = queue.popleft()

        for word in filtered_words:
            if word not in visited and diff(current_word, word):
                if word == end_word:
                    return level + 1
                queue.append((word, level + 1))
                visited.add(word)

    return 0

if __name__ == "__main__":
    n = int(input())
    begin_word = input()
    end_word = input()
    word_list = [input() for _ in range(n)]

    print(ladder_length(n, begin_word, end_word, word_list))

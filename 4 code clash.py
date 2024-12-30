#You are given a dictionary of valid words and a starting word. Your task is to transform the starting word into a target word by changing exactly one letter at a time. Each intermediate word must also be a valid word from the dictionary.You need to find the minimum number of transformations required to convert the starting word to the target word. If it is impossible to transform the word, output -1.
from collections import deque

def min_trans(n, m, w, s, t):
    w_set = set(w)
    if s == t:
        return 0
    q = deque([(s, 1)])
    v = set([s])
    while q:
        w, st = q.popleft()
        for i in range(m):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                nw = w[:i] + ch + w[i+1:]
                if nw == t:
                    return st + 1
                if nw in w_set and nw not in v:
                    v.add(nw)
                    q.append((nw, st + 1))
    return -1

n, m = map(int, input().split())
w = [input().strip() for _ in range(n)]
s, t = input().split()
print(min_trans(n, m, w, s, t))

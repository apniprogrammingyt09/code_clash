#You are given an array of integers arr of size n. A subarray of arr is defined as any contiguous segment of the array. A subarray is considered magical if:
import sys
input = sys.stdin.read

def m(n, k, a):
    c = {0: 1}
    s = 0
    r = 0
    for x in a:
        s += x
        p = s % k
        if p < 0:
            p += k
        r += c.get(p, 0)
        c[p] = c.get(p, 0) + 1
    print(r)

data = input().split()
n, k = int(data[0]), int(data[1])
a = list(map(int, data[2:]))
m(n, k, a)

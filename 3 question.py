#You are given a list of integers. Your task is to sort the integers in ascending order using a binary sorting technique, but with a twist:
def binary_sort(n, arr):
    arr_with_bin = [(bin(x)[2:], x) for x in arr]
    arr_with_bin.sort(key=lambda x: x[0])
    sorted_arr = [x[1] for x in arr_with_bin]
    print(" ".join(map(str, sorted_arr)))



n = 3
arr = [5, 1, 3]

binary_sort(n, arr)

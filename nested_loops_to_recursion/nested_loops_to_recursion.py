def print_numbers(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        print_numbers(idx + 1, arr)


arr = [None] * 3
print_numbers(0, arr)

def find_all_areas(row, col, arr):
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]):
        return 0

    try:
        if arr[row][col] != '-':
            return 0
    except IndexError as e:
        print(e)

    arr[row][col] = 'v'

    current_counter = 1
    current_counter += find_all_areas(row - 1, col, arr)
    current_counter += find_all_areas(row + 1, col, arr)
    current_counter += find_all_areas(row, col - 1, arr)
    current_counter += find_all_areas(row, col + 1, arr)

    return current_counter


arr = [
    ['-', '-', '-', '*', '-', '-', '-', '*', '-'],
    ['-', '-', '-', '*', '-', '-', '-', '*', '-'],
    ['-', '-', '-', '*', '-', '-', '-', '*', '-'],
    ['-', '-', '-', '-', '*', '-', '*', '-', '-'],
]

for row in range(len(arr)):
    for col in range(len(arr[row])):
        size = find_all_areas(row, col, arr)
        if size != 0:
            print(size)

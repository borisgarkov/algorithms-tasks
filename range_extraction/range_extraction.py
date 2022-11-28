def solution(arr):
    if not isinstance(arr, list):
        arr = arr.split(',')

    starting_point = arr[0]
    result = ''
    counter = 1
    skip_number = False

    for number in arr:
        try:
            number = int(number)
        except Exception as e:
            skip_number = True

        if not skip_number and not isinstance(starting_point, int):
            if int(starting_point) + 1 == number:
                counter += 1
                starting_point = number
                if number != arr[-1]:
                    continue

            if counter > 1:
                result += f'-{starting_point}' if counter >= 3 else f',{starting_point}'
                counter = 1
                if number == arr[-1]:
                    continue

        if skip_number:
            result += f',{starting_point}'
            skip_number = False

        starting_point = number
        result += f',{starting_point}'

    return result.strip(',')


print(solution('-86,-85,-83,-81,-79,-77,-76,-73--71,-69,-66,-64,-62,-61'))

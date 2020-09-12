def intersection(arrays):
    result = {}
    for arr in arrays:
        for num in arr:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

    result = [key for key, value in result.items() if value > 1]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

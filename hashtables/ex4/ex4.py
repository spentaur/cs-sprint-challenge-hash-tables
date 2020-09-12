def has_negatives(a):
    res = {}
    for num in a:
        if abs(num) in res:
            res[abs(num)] += 1
        else:
            res[abs(num)] = 1

    return [key for key, value in res.items() if value > 1]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

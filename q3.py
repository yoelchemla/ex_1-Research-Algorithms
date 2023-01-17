from copy import deepcopy


def print_sorted(arr):
    temp = deepcopy(arr)
    return print_sortedR(temp)


def print_sortedR(arr):
    if (isinstance(arr, set) or isinstance(arr, dict)):
        temp_x = dict(sorted(arr.items()))
        for key, val in arr.items():

            # set or dict sorted by key
            if (isinstance(val, set) or isinstance(val, dict)):
                temp_x[key] = print_sortedR(val)
            # list or tuple sort
            elif (isinstance(val, list) or isinstance(val, tuple)):
                arr[key] = val.sort()
        arr = deepcopy(temp_x)
        return arr
    # is a 1 val
    else:
        return arr


if __name__ == "__main__":

    # include 2, 3 sorts or more

    arr = {"a": 5, "c": 6, "b": {2: [2, 1], 3: [2, 1], 1: [2, 1], 4: [2, 1]}}
    print("check 1: " + str(arr))
    print("Sorted arr: " + str(print_sorted(arr)))
    print()

    arr = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print("check 2: " + str(arr))
    print("Sorted arr: " + str(print_sorted(arr)))
    print()

    arr = {"c": 5, "a": {"A": [3, 1], "Z": [0, 2], "C": [4, 1], "B": [2, 0]},
           "b": {1: [6, 1], 3: [4, 0], 2: [9, 1], 4: [9, 1]}}
    print("check 3: " + str(arr))
    print("Sorted arr: ")
    print(str(print_sorted(arr)))
    print()

    arr = {"a": {"a": {"a": {"a": {"b": [0, 7, 1], "a": ["b", "h", "a"]}}}}}
    print("check 4: " + str(arr))
    print("Sorted arr: " + str(print_sorted(arr)))
    print()


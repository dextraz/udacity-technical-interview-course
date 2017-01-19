def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = int((low+high)/2)
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            if high == mid:
                break
            high = mid
    return -1

test = [9, 11, 23, 45, 50, 67, 68, 240, 649, 770, 771, 800]
test_val = 770
print(binary_search(test, test_val))

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array_input):
    if len(array_input) < 2:
        return array_input
    middle = int(len(array_input) / 2)
    left = merge_sort(array_input[:middle])
    right = merge_sort(array_input[middle:])
    return merge(left, right)

print(merge_sort([800, 11, 50, 771, 649, 770, 240, 9, 23, 45, 67, 68]))
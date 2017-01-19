def bubble_sort(array_input):
    changed = True
    while changed:
        changed = False
        if len(array_input) == 1:
            return array_input
        for count, item in enumerate(array_input):

            current_item_index = count
            next_item_index = current_item_index + 1

            if next_item_index < len(array_input):

                next_item = array_input[next_item_index]
                if item > next_item:
                    array_input[next_item_index] = item
                    array_input[current_item_index] = next_item

                    changed = True

    return array_input
print(bubble_sort([800, 11, 50, 771, 649, 770, 240, 9, 23, 45, 67, 68]))
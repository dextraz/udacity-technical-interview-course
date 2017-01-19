def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        current = 1
        previous = 0
        for i in range(0, position-1):
            old_current = current
            old_previous = previous
            previous = old_current
            current = old_current + old_previous

        return current

print(get_fib(9)) # print 34
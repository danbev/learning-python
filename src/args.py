
def some_sum(*some_args):
    result = 0
    for x in some_args:
        result += x
    return result

print(some_sum(1, 2, 3, 4))

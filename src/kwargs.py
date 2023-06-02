
def concat(**kwargs):
    result = ""
    for key, value in kwargs.items():
        print(f'arg: {key}')
        result += value 
    return result

print(concat(a="one", b="two", c="three", e="four"))

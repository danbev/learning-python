
class Something(object):
    def __truediv__(self, other):
        return f'somthing...other:{other}'


s = Something()
print(s / 3)

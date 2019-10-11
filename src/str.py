class Something:
    name = ""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Something(name=' + self.name + ')'

    def __repr__(self):
        return 'Something(name=' + self.name + ')'

s = Something("Fletch")
print(s);

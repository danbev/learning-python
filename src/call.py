class Something:
    def __call__(self, msg):
        print(msg)

s = Something()
s("bajja");
s.__call__("bajja");

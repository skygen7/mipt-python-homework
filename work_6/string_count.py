class MyClass:

    FILE = r'out.txt'

    def __init__(self, string):
        self.string = string
        self.count = self.string.count('A')
        # self.run()

    def run(self, *args, **kwargs):
        print(self.count, file=open(self.FILE, 'w'))


with open(r'in.txt') as f:
    ex = MyClass(f.readline())
    ex.run()

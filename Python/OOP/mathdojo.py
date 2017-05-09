class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for each in args:
            self.result += each
        return self
    def subtract(self, *args):
        for each in args:
            self.result -= each
        return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result
md = MathDojo()

md.add(2).add(2, 5).subtract(3, 2).result

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

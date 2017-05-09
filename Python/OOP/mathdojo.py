class MathDojo(object):
    """calculator for adding and subtracting"""
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for x in args:
            if isinstance(x, list) or isinstance(x, tuple):
                for y in x:
                    self.result += y
            else:
                self.result += x
        return self
    def subtract(self, *args):
        for x in args:
            if isinstance(x, list) or isinstance(x, tuple):
                for y in x:
                    self.result -= y
            else:
                self.result -= x
        return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

md = MathDojo()
print md.add([1],3,4).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print md.add(2).add(2, 5).subtract(3, 2).result

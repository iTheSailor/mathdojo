class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            self.result += arg
        return self
    def subtract(self, *args):
        for arg in args:
            self.result -= arg
        return self
    
md = MathDojo()
x=md.add(2).add(2,5).subtract(3,2,16,122).result
print(x)
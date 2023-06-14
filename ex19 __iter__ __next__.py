print(list(range(0, 4, 1)))
a9 = iter(range(5))
next(a9)

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)
print(fr.__next__())
print(fr.__next__())
print(next(fr))
print(next(fr))
print(next(fr))
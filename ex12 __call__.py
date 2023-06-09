class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step = 1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter

    def get_counter(self):
        return self.__counter

c = Counter()
c1 = Counter()
c1()
c(10)
c(2)
res = c1(-5)
res1 = c()
print(res, res1)
class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
         self.x = x
         self.y = y

    def set_coords(self, x, y):
         self.x = x
         self.y = y

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

pt1 = Point(1,2)
pt2 = Point(10,20)
a = pt1.y
class Point2D:
    __slots__ = ('x', 'y', '__length')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x*x + y*y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt = Point2D(1, 2)
print(pt.length)
pt.length = 1000
print(pt.length)

pt1 = Point3D(10, 20, 25)
pt1.z = 30
print(pt1.z, pt1.__slots__, pt1.x)


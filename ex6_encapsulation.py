class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        print(self.__x, self.__y)

    def set_coords(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coords(self):
        return self.__x, self.__y

pt = Point(1,2)
pt.set_coords(10,4)
print(pt.get_coords())

print(type(float))
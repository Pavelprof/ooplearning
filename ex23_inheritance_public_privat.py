class Geom:
    __name = 'Geom'
    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom для {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self):
        return (self._x1,self._y1)

r = Rect(0,0,10,20)
print(r.__dict__)

print(r.get_coords())
print(r._x1)
print(r._name)
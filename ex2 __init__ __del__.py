class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=124, y=543):
        print('вызов __init__')
        self.x = x
        self.y = y

    def __del__ (self):
        print("удаление экземпляра:", str(self))
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
print(pt.__dict__)
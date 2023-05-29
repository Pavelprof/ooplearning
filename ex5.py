class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, a, b):
        self.x = self.y = 0
        if self.validate(a) and self.validate(b):
            self.x = a
            self.y = b

    def get_coords(self):
        return self.x, self.y

v = Vector(11,7)
res = Vector.get_coords(v)
print(res)
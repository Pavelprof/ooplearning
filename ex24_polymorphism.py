class Geom:
    def get_pr(self):
        raise NotImplementedError('The child class should redefine the method get_pr')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

#    def get_pr(self):
#       return 4 * self.a

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
sq1 = Square(10)
sq2 = Square(20)

geom = [r1, r2, sq1, sq2]

for g in geom:
    print(g.get_pr())


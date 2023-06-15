# class Geom:
#     pass
#
# class Line(Geom):
#     pass
#
#
# g = Geom()
# l = Line()
#
# print(Geom.__name__)
# print(g)
# print(l.__class__)
# print(issubclass(Line, Geom))
# print(issubclass(Geom, Line))
# print(isinstance(l, Geom))
# print(isinstance(l, object))
# print(isinstance(Geom, object))
# print(issubclass(list, object))

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector((1,2,3,4))
print(v)
print(type(v))
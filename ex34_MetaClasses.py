class Point:
    MAX_COORD = 100
    MIN_COORD = 0

class B1: pass
class B2: pass

def method1(self):
    print(self.__dict__)

A = type('Point', (B1, B2), {"MAX_COORD" : 100, "MIN_COORD" : 0, "method1" : method1})

pt = A()

pt.method1()

A.__mro__
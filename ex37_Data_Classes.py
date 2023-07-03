from dataclasses import dataclass, field
from pprint import pprint

class Thing:
    def __init__(self, name, weight, price, dims = []):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'Thing: {self.__dict__}'

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

# t = Thing('Python book', 100, 400)
# print(t.get_name())
# print(t.__dict__)
# t.dims.append(10)
# print(t.dims)
#
# t2 = Thing('Python book', 111, 400)
# print(t2.dims)
# print(t.weight)

td = ThingData('Java book', 120, 420)
td1 = ThingData('Java book', 120)
print(td)
# pprint(ThingData.__dict__)
print(td == td1)
print(ThingData)
td.dims.append(11)
print(td.dims)
print(td1.dims)
from dataclasses import dataclass
from pprint import pprint

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'Thing: {self.__dict__}'

@dataclass
class ThingData:
    name: str
    weight: int
    price: float

t = Thing('Python book', 100, 400)
print(t.get_name())
print(t)

td = ThingData('Java book', 120, 420)
print(td)
pprint(ThingData.__dict__)
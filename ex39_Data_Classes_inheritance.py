from dataclasses import dataclass, field, InitVar
from typing import Any

class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0,0,0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init = False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: __post_init__")
        Goods.current_uid += 1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    @staticmethod
    def get_init_measure():
        return [0,0,0]

    def __post_init__(self):
        super().__post_init__()
        print("Book: __post_init__")

b = Book(200, 1, 'bookk', 'Jason')
print(b)

c = Book(1)
print(c)


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed



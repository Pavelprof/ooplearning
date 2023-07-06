from dataclasses import dataclass, field, InitVar
from typing import Any

@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init = False)
    price: Any = None
    weight: Any = None

@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0

b = Book(123, 200, 1, 'bookk', 'Jason')
print(b)

c = Book(1)
print(c)
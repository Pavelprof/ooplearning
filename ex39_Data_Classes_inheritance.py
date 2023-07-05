from dataclasses import dataclass, field, InitVar
from typing import Any

@dataclass
class Goods:
    uid: Any
    price: Any = None
    weight: Any = None
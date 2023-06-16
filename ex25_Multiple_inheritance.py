class Goods:
    def __init__(self, name, weight, price):
        print("init Goods")
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')

class MixinLog:
    ID = 0

    def __init__(self):
        print('init MixinLog')
        super().__init__()
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_cell_log(self):
        print(f'{self.id}: good was sold at 00:00 hours')

    def print_info(self):
        print(f'print_info_from_MixinLog')

class MixinLog2:
    def __init__(self):
        print('init MixinLog2')
        super().__init__()

class Notebook(Goods, MixinLog2, MixinLog):
    def print_info(self):
        MixinLog.print_info(n)

n = Notebook('Acer', 3.5, 30000)
n.save_cell_log()
print(Notebook.__mro__)

n.print_info()
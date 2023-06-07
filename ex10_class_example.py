from string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise typeError("FIO should be string")

        f = fio.split()
        if len(f) != 3:
            raise typeError("Please correct the format of FIO")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('Type at least one simbol')
            if
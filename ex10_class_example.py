from string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)
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
                raise TypeError('Please, type at least one character')
            if len(s.strip(letters)) != 0:
                raise TypeError('Please, use only allowed characters')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old >120:
            raise TypeError('Age should be integer between 14 and 120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) not in (int, float) or w < 20:
            raise TypeError('Weight should be integer or float from 20')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Passport must be string')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
            raise TypeError('Wrong passport forma')


p = Person('ВАсилукп Павеле Ленавмвваи', 33, '3234 234543', 80)
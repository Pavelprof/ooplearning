from string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
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

        for p in s:
            if not p.isdigit():
                raise TypeError('Passport should include only digits')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return  self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return  self.__weight

    @weight.setter
    def weight(self, w):
        self.verify_weight(w)
        self.__weight = w

    @property
    def passport(self):
        return  self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

p = Person('ВАсилукп Павеле Ленавмвваи', 33, '3234 234543', 80)
print(p.__dict__)
p.old = 50
p.passport = '8230 000000'
print(p.__dict__)
class Women:
    title = 'Class object for title field'
    photo = 'Class object for photo field'
    ordering = 'Class object for photo field'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access

print(Women.ordering)
print(Women.Meta.ordering)

w = Women('Julia', "123")
print(w.ordering)
print(w.Meta.ordering)
print(w.meta.__dict__)

m = w.Meta(123)
print(m.ordering)

print(w.__dict__)
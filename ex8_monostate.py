class ThreadData:
    _shared_attrs = {
        'name': 'thread1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self._shared_attrs

th1 = ThreadData()
th2 = ThreadData()
th2.id = 3
th1.new_attr = 'new_attr'
print(ThreadData._shared_attrs)
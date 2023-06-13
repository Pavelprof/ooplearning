class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if item not in self.marks:
            raise IndexError("Incorrect Index")
        return self.marks[item]

    def __setitem__(self, key, value):
        self.marks[key] = value

    def __delitem__(self, key):
        self.marks[key] = None

s1 = Student('Alan', [3,6,4,8,2])
print(s1[2])

s1[2] =10
print(s1[2])
print(s1.marks)

del s1[1]
print(s1.marks)
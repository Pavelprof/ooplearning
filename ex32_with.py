# fp = None
# try:
#     with open("myfile.txt") as fp:
#         for t in fp:
#             print('t')
# except Exception as e:
#     print(e)

class DefendedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False

v1 = [1, 2, 3]
v2 = [4, 5, 6]

dvv = DefendedVector(v1)
dvv._DefendedVector__v[0] = 8
print(dvv._DefendedVector__v)
print(v1)

try:
    with DefendedVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]

except:
    print('Error')

print(v1)
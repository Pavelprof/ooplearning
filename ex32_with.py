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


v1 = [1, 2, 3]
v2 = [4, 5]

with DefendedVector(v1) as dv:
    for i in enumerate(dv):
        dv[i] += v2[i]

print(v1)
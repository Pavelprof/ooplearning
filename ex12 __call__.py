class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Argument should be string')

        return args[0].strip(self.__chars)

    def get_counter(self):
        return self.__counter


s1 = StripChars('?:!.; ')
res = s1(' !Hello world!;')
print(res)
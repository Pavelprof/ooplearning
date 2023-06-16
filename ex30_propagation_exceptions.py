try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError:
    print('x/0 What are you doing?')
except ValueError as z:
    print(z)
else:
    print('There are no exceptions')
finally:
    print('I will print it anyway')
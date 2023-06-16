try:
    x, y = map(int, input().split())
    res = 1 / 0
except ZeroDivisionError:
    print('x/0 What are you doing?')
except ValueError:
    print('incorrect value')


print('\nI am still working')
print('OK, I am sleeping')
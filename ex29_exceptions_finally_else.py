# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print('x/0 What are you doing?')
# except ValueError as z:
#     print(z)
# else:
#     print('There are no exceptions')
# finally:
#     print('I will print it anyway')

def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print('Finally execute before return')

x, y = get_values()
print(x, y)
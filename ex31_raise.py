# print('egrgt 3rherh 3h5t54 35h3 h3')
# print('egrgt 3rherergrh 3h 35h3 h3')
# print('egrgt 3rergherh 3h 35h3 h3')
# print('egrgtege 3rherh 3h 35h3 h3')
# e = ZeroDivisionError('Zero division')
# raise e
# print('egrgt 3rherhsvfe 3h 35h3 h3')
# print('egrgt 3rherh 3h 35qegeh3 h3')
# print('egrgt 3rherh 3h 35h3 h3')

class ExceptionPrint(Exception):
    """The class for all printer errors"""

class ExceptionPrintSendData(ExceptionPrint):
    '''The class of exceptions for errors of printer data sending'''
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Printer is unavailable')

    def send_to_print(self, data):
        return False

p = PrintData()

# p.print('wfwe')

try:
    p.print('wfwe')
except ExceptionPrintSendData:
    print('Data is not sending')
except ExceptionPrint:
    print('It\'s not working')
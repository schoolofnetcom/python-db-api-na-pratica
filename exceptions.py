# #a = 1/0
# try:
#     #b[1]
#     #a = 1/0
#     #raise ZeroDivisionError('lançei um erro')
#     raise NameError('lançei outro erro')
# except ZeroDivisionError as inst:
#     print(inst)
#     print('Divisao por zero')
# except NameError:
#     print('erro com b[1]')

class AppException(Exception):
    pass

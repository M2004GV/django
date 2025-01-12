#pdb 
import pdb
import logging

x = [1, 2, 3]
y = 2
z = 3

#pdb.set_trace()
#print(x + z)

#tratamento de erros
# try:
#     print(x + z)
# except Exception as e:
#     print('Erro: {}'.format(e))


#logging
logging.basicConfig(filename="app.log", level = logging.DEBUG)

log = logging.getLogger()

log.info('Olá')
print(log.level)
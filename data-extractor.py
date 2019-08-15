arquivo = open('c:/py/1.txt', 'r')

data = arquivo.read()

arr = data.split('|')
print(arr)
arquivo.close
arquivo = open('c:/py/1.txt', 'r')

for line in arquivo: 
    print(line.split('|'))


arquivo.close
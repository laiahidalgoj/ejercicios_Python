def createFile(file):
    f = open(file, 'x')
    f.close()

createFile('text.txt')

def writeFile(file, data):
    f = open(file, 'w')

    for line in data:
        f.write(line)
    f.close()

text = 'hola, esto es un texto de prueba'

writeFile('text.txt', text)

print(text)
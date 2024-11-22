name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except FileNotFoundError:
    print("File not found:", name)
    exit()

di = dict()  # Diccionario para contar correos electrónicos

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):  # Solo procesar líneas que empiezan con 'From '
        continue
    wds = line.split()
    if len(wds) > 1:  # Verificar que haya un correo en la línea
        email = wds[1]
        di[email] = di.get(email, 0) + 1  # Contar las apariciones del correo

# Encontrar el correo más frecuente
largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k

print(theword, largest)

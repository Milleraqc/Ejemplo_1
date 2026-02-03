
dec = int(input('Ingrese un numero entre 0 e infinito y más allá: '))
binario = ""

while (dec > 0):
    bin = dec % 2
    binario = str(bin) + binario
    dec //= 2

print(binario)
# %%

dec = int(input('Ingrese un numero entre 0 e infinito: '))
binario = ""

while (dec > 0):
    bin = dec % 2
    binario = str(bin) + binario
    dec //= 2
binario = int(binario)
print(binario)

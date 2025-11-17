CPB = 0.25
CEG = 0.29
print('calcular el flete')
peso = input('ingrese el peso:')
flete = float(peso) * CPB
flete1 = float(peso) * CEG
margen = flete1 - flete

print('flete proveedro',flete)
print('flete local', flete1)
print('margen',margen)

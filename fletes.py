cpb = 0.25
ceg = 0.31
cf = 0.354   
peso = 15904.602

print('calcular el flete')
#peso = input('ingrese el peso:')
flete_pablo = float(peso) * cpb
flete_cobrado = float(peso) * ceg
flete_final = float(peso) * cf

print('flete pablo',flete_pablo)
print('flete cobrado',flete_cobrado)
print('flete ted',flete_cobrado - flete_pablo)
print('flete final',flete_final)
print("costo x kilo",flete_final / peso)
print("diferncia",flete_final - flete_cobrado)
print('flete con aumento',flete_cobrado + 700)
print("flete invluido igv",flete_final * 1.18)
print("***************************************")
print("flete plabo mas aumento",flete_pablo + 700)
print("ted",peso*0.06)
print("pablo",peso*0.294)



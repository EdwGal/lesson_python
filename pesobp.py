CONSTANTEEJE = 0.0062
CONSTANTEPL = 7.85
def pesobarra(d1, long1):
    peso_barra = d1*d1*CONSTANTEEJE*long1
    return peso_barra    

def pesoplancha(esp1, ancho, largo):
    peso_plancha=esp1*ancho*largo*CONSTANTEPL
    return peso_plancha

def operaciones():
    print("QUE DESEAS CALCULAR")
    print("====================================")
    print("1. PESO DE UNA BARRA")
    print("2. PESO DE UNA PLANCHA")
    print("3. PESO DE VIGAS Y CANALES")
    print("4. PESO DE BARRAS CUADRADAS")
    opcion = input('INGRESE LA OPCION:')
    opcion = int(opcion)
    if opcion == 1:
        diametro_1 = float(input('Ingrese diametro: '))
        longitud = float(input('Ingrese longitud: '))
        print("El peso de la barra es : ", round(pesobarra(diametro_1,longitud),4),"kgs", "\n")
    elif opcion == 2:
        espesor = float(input('ingrese el espesor de la plancha: '))
        ancho = float(input('ingrese el ancho:'))
        largo = float(input('ingres el largo:'))
        print('El peso de laplancha es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opcion == 3:
        espesor = float(input('ingrese el espesor de la plancha: '))
        ancho = float(input('ingrese el ancho:'))
        largo = float(input('ingres el largo:'))
        print('El peso de una viga es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    else:
        espesor = float(input('ingrese el espesor de la plancha: '))
        ancho = float(input('ingrese el ancho:'))
        largo = float(input('ingres el largo:'))
        print('El peso de una barra cuadrada es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
operaciones()        
print('Gracias por usar nuestro app')
opc = input('desea continuar S/N')
if opc == "S":
    

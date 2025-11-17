op = "s"
i = True
CONSTANTEEJE = 0.0062
CONSTANTEPL = 7.85
IGV = 0.18
def pesobarra(d1, long1):
    peso_barra = d1*d1*CONSTANTEEJE*long1
    return peso_barra    

def pesoplancha(esp1, ancho, largo):
    peso_plancha=esp1*ancho*largo*CONSTANTEPL
    return peso_plancha

def igv(ptot):
    STot = ptot / 1.18
    igv = STot * IGV
    return STot, igv

while  i == True:
    print("QUE DESEAS CALCULAR")
    print("====================================")
    print("1. PESO DE UNA BARRA")
    print("2. PESO DE UNA PLANCHA")
    print("3. PESO DE VIGAS Y CANALES")
    print("4. PESO DE BARRAS CUADRADAS")
    print("5. IGV")
    print("6. PRECIO CON MARGEN")
    print("7. SALIR")
    opc = int (input("escoje la opcion :"))
    if opc == 1:
        diametro_1 = float(input('Ingrese diametro: '))
        longitud = float(input('Ingrese longitud: '))
        print("PESO DE LA BARRA ES: ", round(pesobarra(diametro_1,longitud),4),"kgs", "\n")
    elif opc == 2:
        espesor = float(input('ingrese el espesor de la plancha: '))
        ancho = float(input('ingrese el ancho:'))
        largo = float(input('ingres el largo:'))
        print('PESO DE LA PLANCHA ES: ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opc == 3:
        print("estamos trabajando en el modulo")
    elif opc == 4:
        print("estamos trabajando en el modulo")
    elif opc == 5:
        PreTotal = float(input('ingrese el precio total: '))
        valores = igv(PreTotal)
        print("************************")
        print("SUB-TOTAL: ",round(valores[0],2))
        print("IGV      : ",round(valores[1],2))
        print("TOTAL    : ",PreTotal)
        print("************************")
        #largo = float(input('ingres el largo:'))
        #print('El peso de laplancha es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opc == 6:
        PrecProvedor = float(input('ingrese el precio del material del  proveedor: '))
        PesoMaterial = float(input('ingrese el peso del Material:'))
        ValMargen = float(input('ingres el Margen a calcular:'))
        ValMargen = ValMargen/100
        ValMargen = 1- ValMargen
        print('precio x kilo proveedor', PrecProvedor/PesoMaterial)
        print('precio con margen ', ((PrecProvedor/PesoMaterial)/ValMargen))
        PrecioFinal = (PrecProvedor/PesoMaterial)/(ValMargen)
        print('El precio con un marge de', ValMargen , 'es : ', round((PrecioFinal), 4),'kgs','\n')
    elif opc ==7:
        op = str(input("DESEA SALIR DEL APP s/n :"))
        if op == "s":
            i=False
            print("gracias por su visita")
        else:
            i=True

        
        
    
    
    
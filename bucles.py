op = "s"
i = True
CONSTANTEEJE = 0.0062
CONSTANTEPL = 7.85
PI = 3.1416
IGV = 0.18
opc = 0
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
    print("3. PESO BARRA PERFORADA")
    print("4. PESO DE BARRAS CUADRADAS")
    print("5. IGV")
    print("6. PRECIO CON MARGEN")
    print("7. PESO DE VIGAS Y CANALES")
    print("8. AUMENTO DE PRECIO PORCENTUAL")
    print("9. SALIR")
    opc = int (input("Escoje la opcion : "))
    if opc == 1:
        diametro_1 = float(input('Ingrese Diametro: '))
        longitud = float(input('Ingrese Longitud: '))
        print("PESO DE LA BARRA ES: ", round(pesobarra(diametro_1,longitud),4),"kgs", "\n")
    elif opc == 2:
        espesor = float(input('Ingrese el Espesor de la Plancha: '))
        ancho = float(input('Ingrese el Ancho:'))
        largo = float(input('Ingrese el Largo:'))
        print('PESO DE LA PLANCHA ES: ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opc == 3:
        print("estamos trabajando en el modulo")
        d_Ext = float(input('Ingrese el Diametro Exterior: '))
        d_Int = float(input('Ingrese el Diametro Interior: ')) 
        longitud = float(input('Ingrese Longitud: '))
        area  = (PI/4)*(d_Ext*d_Ext - d_Int*d_Int)
        print("AREA ES: ", round(area,4),"cm2", "\n")
        volumen = area * longitud
        print("VOLUMEN ES: ", round(volumen,4),"cm3", "\n")
        peso = (volumen * CONSTANTEPL)/1000
        print("PESO DE LA BARRA PERFORADA ES: ", round(peso,4),"kgs", "\n") 
        
        
    elif opc == 4:
        print("estamos trabajando en el modulo")
    elif opc == 5:
        PreTotal = float(input('Ingrese Precio Total: '))
        valores = igv(PreTotal)
        print("************************")
        print("SUB-TOTAL: ",round(valores[0],2))
        print("IGV      : ",round(valores[1],2))
        print("TOTAL    : ",PreTotal)
        print("************************")
        #largo = float(input('ingres el largo:'))
        #print('El peso de laplancha es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opc == 6:
        PrecProvedor = float(input('Ingrese Precio del Material del Proveedor: '))
        PesoMaterial = float(input('Ingrese Peso del Material:'))
        ValMargen = float(input('Ingrese el Margen a Calcular:'))
        ValMargen = ValMargen/100
        ValMargen = 1- ValMargen
        print('Precio x Kilo Proveedor', PrecProvedor/PesoMaterial)
        print('Precio con Margen ', ((PrecProvedor/PesoMaterial)/ValMargen))
        PrecioFinal = (PrecProvedor/PesoMaterial)/(ValMargen)
        print('El precio con un marge de', ValMargen , 'es : ', round((PrecioFinal), 4),'kgs','\n')
    elif opc == 7:
        print("estamos trabajando en el modulo")
    elif opc == 8:
        pre_ant = float(input('Ingrese el Precio Anterior: '))
        pre_act = float(input('Ingrese el Precio Actual: '))
        aumento = ((pre_act - pre_ant) / pre_ant) * 100
        print('El aumento porcentual es de: ', round(aumento, 2), '%', '\n')
    elif opc == 9:
        op = str(input("DESEA SALIR DEL APP s/n :"))
        if op == "s":
            i=False
            print("gracias por su visita")
        else:
            i=True

        
        
    
    
    
import os


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

def bperforada():
    d_Ext = float(input('Ingrese el Diametro Exterior: '))
    d_Int = float(input('Ingrese el Diametro Interior: ')) 
    longitud = float(input('Ingrese Longitud: '))
    area  = (PI/4)*(d_Ext*d_Ext - d_Int*d_Int)
    print("***** RESULTADO DE LOS OPERACIONES *******")
    print("AREA ES: ", round(area,4),"cm2", "\n")
    volumen = area * longitud
    print("VOLUMEN ES: ", round(volumen,4),"cm3", "\n")
    peso = (volumen * CONSTANTEPL)/1000
    print("PESO DE LA BARRA PERFORADA ES: ", round(peso,4),"kgs", "\n")
    return
 
def menu():
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
    return

def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')
        
while  i == True:
    
    if opc == 0:
        menu()
        opc = int (input("Escoje la opcion : "))
        limpiar_pantalla()    
    else:
        i = False    
    
    if opc == 1:       
        print("\n***** INGRESE PARAMETROS *******\n")
        diametro_1 = float(input('Ingrese Diametro: '))
        longitud = float(input('Ingrese Longitud: '))
        print("\n***** RESULTADO DE LA OPERACION *******\n")
        print("PESO DE LA BARRA ES: ", round(pesobarra(diametro_1,longitud),4),"kgs", "\n")
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 2:
        print("\n***** INGRESE PARAMETROS *******\n")
        espesor = float(input('Ingrese el Espesor de la Plancha: '))
        ancho = float(input('Ingrese el Ancho:'))
        largo = float(input('Ingrese el Largo:'))
        print("\n***** RESULTADO DE LA OPERACION *******\n")
        print('PESO DE LA PLANCHA ES: ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 3:
        print("\n***** INGRESE PARAMETROS *******\n")
        bperforada()
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
        
    elif opc == 4:
        print("\n estamos trabajando en el modulo \n")
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 5:
        print("\n***** INGRESE PARAMETROS ******* \n")
        PreTotal = float(input('Ingrese Precio Total: '))
        valores = igv(PreTotal)
        print("\n***** RESULTADO DE LAS OPERACIONES ********\n")
        print("SUB-TOTAL: ",round(valores[0],2))
        print("IGV      : ",round(valores[1],2))
        print("TOTAL    : ",PreTotal)
        print("********************************************")
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
        #largo = float(input('ingres el largo:'))
        #print('El peso de laplancha es de : ', round(pesoplancha(espesor,ancho,largo), 4),'kgs','\n')
    elif opc == 6:
        print("\n****************** INGRESE PARAMETROS **********************\n")
        PrecProvedor = float(input('Ingrese Precio del Material del Proveedor: '))
        PesoMaterial = float(input('Ingrese Peso del Material:'))
        ValMargen = float(input('Ingrese el Margen a Calcular:'))
        ValMargen = ValMargen/100
        ValMargen = 1- ValMargen
        print("\n****************** RESULTADO DE LAS OPERACIONES ************\n")
        print('Precio x Kilo Proveedor', PrecProvedor/PesoMaterial)
        print('Precio con Margen ', ((PrecProvedor/PesoMaterial)/ValMargen))
        PrecioFinal = (PrecProvedor/PesoMaterial)/(ValMargen)
        print('El precio con un marge de', ValMargen , 'es : ', round((PrecioFinal), 4),'kgs','\n')
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 7:
        print("\n estamos trabajando en el modulo \n")
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 8:
        print("\n***** INGRESE PARAMETROS *******\n")
        pre_ant = float(input('Ingrese el Precio Anterior: '))
        pre_act = float(input('Ingrese el Precio Actual: '))
        aumento = ((pre_act - pre_ant) / pre_ant) * 100
        print("\n***** RESULTADO DE LAS OPERACIONES ********\n")
        print('El aumento porcentual es de: ', round(aumento, 2), '%', '\n')
        os.system('pause')
        limpiar_pantalla()
        i = True
        opc = 0
    elif opc == 9:
        op = str(input("DESEA SALIR DEL APP s/n :"))
        if op == "s":
            i=False
            print("gracias por su visita")
        else:
            i=True
            opc = 0

        
        
    
    
    
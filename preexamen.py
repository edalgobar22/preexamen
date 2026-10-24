"""

"""
def depositar (saldo, deposito):
    if deposito < 0:
        print("Los numeros tienen que ser reales positivos")
        input("Presione Enter para volver al menu anterior...")
    elif deposito == 0:
        return saldo 
    else:    
        saldo = saldo + deposito
        print("Deposito realizado\nSu saldo es: ", saldo) 
        input("Presione Enter para volver al menu anterior...")
    return saldo

def retirar (saldo, retiro):
    if retiro > saldo:
        print("Saldo insuficiente")
        input("Presione Enter para volver al menu anterior...")
    elif retiro < 0:
        print("Los numeros tienen que ser reales positivos")
        input("Presione Enter para volver al menu anterior...")
    elif retiro == 0:
        return saldo    
    else:
        saldo = saldo - retiro
        print("Retiro realizado\nSu saldo es: ", saldo)
        input("Presione Enter para volver al menu anterior...")
    return saldo
    
    
opcion = -1
saldo = 1000
while opcion != 4 and opcion !=0:
    print("""
    ==== MENU ===
    1. Consultar saldo
    2. Depositar dinero
    3. Retirar dinero
    4. Salir
    """)
    opcion = int(input("Seleccione una opcion?: "))
    if opcion > 4:
        input("Opcion invalida\nPresione Enter para continuar...")
    match opcion:
        case 1:
            print("Su saldo es: ", saldo)
            input("Presione Enter para continuar...")
        case 2:
            deposito = int(input("Cuanto va a depositar?: "))
            saldo = depositar (saldo, deposito)
           
        case 3:
            retiro = float(input("Cuanto va a retirar?: "))
            saldo = retirar(saldo, retiro)
        case 4:
            print("Gracias por su visita")
        case 0:
            print("Gracias por su visita")    

            
            
    
#Ejemplo de condicion de carrera

#Librerias
import threading
from time import sleep
import threading 
import time


#objeto de pago
user={
    "full_name": "Jose Ali Mendoza Armas",
    "product": "Articulo 1 ",
    "price":"$3500.34",
    "shop": "Walmart",
    "paid": None,
    "brand" : "visa",
    "checks": {
        "address_line1_check": "null",
        "address_postal_code_check": "null",
        "cvc_check": "unchecked"
    },
}


#Simulacion de interfaz de confirmacion de pago de cliente
def UI():  
    print("-------------------------------------------------------------")
    print("========================= Factura ===========================")
    print("-------------------------------------------------------------")
    print("Tienda", user.get("shop"), "Producto: ",user.get("product"))
    print("Tarjeta",user.get("brand"), "Monto: ",user.get("price")) 
    print("Nombre: ",user.get("full_name"))
    print("_____________________________________________________________")
    time.sleep(5)
    if user.get("paid") is True :
        print("Pago efectuado")
    else :
        print("Pago rechazado")


#Simulacion de notificacion de token del usuario 
def notification():
    print("----- Autentificacion de compra ----")
    print("Confirme si usted a realizado esta compra")
    print("1.-SI/2.-NO")
    access = input()
    if access is "1" :
        user.update({'paid': True})
    else :
        if access is "2":
            user.update({'paid ':False })


# #Creacion de los hilos
t = threading.Thread(target=UI)
t2 =threading.Thread(target=notification)
# # Ejecutar los hilos
t.start()
t2.start()

#notification()
#print(user)









































__autor__ = "Jose Ali Mendoza Armas"
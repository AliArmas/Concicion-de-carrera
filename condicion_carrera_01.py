#Ejemplo de condicion de carrera

#Librerias

import threading
from time import sleep
from threading import Thread, Timer
import multiprocessing
import random
import time
from typing_extensions import Self

#objeto de pago

user={
    "full_name": "Jose Ali Mendoza Armas",
    "product": "Articulo 1 ",
    "price":"$3500.34",
    "shop": "Walmart",
    "paid": True,
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
    print("==================== Factura de Microsoft ===================")
    print("-------------------------------------------------------------")
    print("Tienda", user.get("shop"), "Producto: ",user.get("product"))
    print("Tarjeta",user.get("brand"), "Monto: ",user.get("price")) 
    print("Nombre: ",user.get("full_name"))
    print("_____________________________________________________________")
    time.sleep(2)
    if user.get("paid") is True :
        print("Pago efectuado")
    else :
        print("Pago rechazado")

def notification():
    print("----- Autentificacion de compra ----")
    print("Confirme si usted a realizado esta compra")
    print("1.-SI/2.-NO")
    access = input()
    if access is "2" :
        print("Cambio")
        user.update({'paid': False})


# #Creacion de los hilos
t = threading.Thread(target=UI)
t2 =threading.Thread(target=notification)
# # Ejecutar los hilos
t.start()
t2.start()

#notification()
#print(user)









































__autor__ = "Jose Ali Mendoza Armas"
#Ejemplo de condicion de carrera

#Librerias

from time import sleep
from threading import Thread
import multiprocessing
import random

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
    if user.get("paid") is True :
        print("Pago efectuado")
    else :
        print("Pago rechazado")

def notification():
    print("----- Autentificacion de compra ----")
    print("Confirme si usted a realizado esta compra")
    print("1.-SI/2.-NO")
    access = input()
    if access is 2 :
        user.update({'paid': False})



notification()

print(user  )










































__autor__ = "Jose Ali Mendoza Armas"
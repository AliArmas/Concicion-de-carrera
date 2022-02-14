# Condicion-de-carrera

Programa que simula la de **condición de carrera** en programacion concurrente en el lenguaje de Python

--- 

# ¿Qué es una condición de carrera?

Se produce una condición de carrera cuando dos subprocesos intentan acceder a una variable compartida simultáneamente.

El primer hilo lee el valor de la variable compartida. El segundo hilo también lee el mismo valor de la variable compartida.

Luego, ambos hilos intentan cambiar el valor de la variable compartida. Y corren para ver qué hilo escribe un valor en la variable en último lugar.

El valor del hilo que escribe en la última variable compartida se conserva porque sobrescribe el valor que escribió el hilo anterior.

# Problematica



## Objetivos
+ Notificarle al usuario las compras realizadas
+ Salvaguardar los datos del cliente
+ Mejorar la seguridad pay to pay

---

## Librerias utilizadas 📦️

_Las librerias utilizadas estan basadas en el mejor manejo y optimizacion de codigo en la version de python 3.8_

```
import os
import time
import threading
import multiprocessing
 
```




---
con ❤️ por [AliArmas](https://github.com/AliArmas) 🧑‍💻

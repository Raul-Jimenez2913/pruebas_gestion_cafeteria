#Created by: Christian Raúl Jiménez Hernández - AO1736302
#Pruebas Sistema de Gestión de Cafetería

import pytest
from Gestion_cafeteria import agregar_bebida 

# 1) El nombre del artículo es alfabético (válido)
def test_alfabetico():
    assert agregar_bebida("Latte,1,2,3") == True
    assert agregar_bebida("Cafe,1,2,3") == True
    assert agregar_bebida("Te,4,5") == True
    assert agregar_bebida("Cafe123,1,2") == False
    assert agregar_bebida("123,1") == False
    assert agregar_bebida("Café,1,2") == True
    
# 2) El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)
def test_2caracteres():
    assert agregar_bebida("L,1,2") == False
    assert agregar_bebida("A,1,2,3") == False
    assert agregar_bebida(",1,2") == False
    assert agregar_bebida("B,4,5") == False
    assert agregar_bebida("Al,1,2") == True
    assert agregar_bebida("Tea,3,4") == True

# 3) El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)
def test_longitud():
    assert agregar_bebida("Americano,1,2,3,4,5") == True
    assert agregar_bebida("Espresso,1,2,3") == True
    assert agregar_bebida("Latte,4,5") == True
    assert agregar_bebida("CappuccinoMochaLatte,1") == False
    assert agregar_bebida("Cortado,6") == True
    assert agregar_bebida("CaffeAmericano,1,2") == True

# 4) El valor del tamaño está en el rango de 1 a 48 (válido)
def test_tamano():
    assert agregar_bebida("Espresso,1,48") == True
    assert agregar_bebida("Mocha,1") == True
    assert agregar_bebida("Latte,48") == True
    assert agregar_bebida("Tea,0") == False
    assert agregar_bebida("Tea,49") == False
    assert agregar_bebida("Tea,-1") == False

# 5) El valor del tamaño es un número entero (válido)
def test_tamano_entero():
    assert agregar_bebida("Mocha,10") == True
    assert agregar_bebida("Espresso,2") == True
    assert agregar_bebida("Americano,3,4") == True
    assert agregar_bebida("Capuccino,2.5") == False
    assert agregar_bebida("Mocha,2a") == False
    assert agregar_bebida("Latte,x") == False

# 6) Los valores del tamaño se ingresan en orden ascendente (válido)
def test_tamanos_orden_ascendente():
    assert agregar_bebida("Capuccino,1,2,3,4,5") == True
    assert agregar_bebida("Americano,1,2,3,4,5") == True
    assert agregar_bebida("Latte,10,20,30") == True
    assert agregar_bebida("Cappuccino,3,2") == False
    assert agregar_bebida("Mocha,5,3,4") == False
    assert agregar_bebida("Espresso,4,4") == False  # No es estrictamente ascendente

# 7) Se ingresan de uno a cinco valores de tamaño (válido)
def test_cantidad_tamanos():
    assert agregar_bebida("Frappe,1,2,3") == True
    assert agregar_bebida("Solo,1") == True
    assert agregar_bebida("Doble,1,2") == True
    assert agregar_bebida("Triple,1,2,3") == True
    assert agregar_bebida("Cuadruple,1,2,3,4") == True
    assert agregar_bebida("Quintuple,1,2,3,4,5") == True

# 8) El nombre del artículo es el primero en la entrada (válido)
def test_nombre_no_primero():
    assert agregar_bebida("1,Latte,2,3") == False
    assert agregar_bebida("Cafe,1,2,3") == True
    assert agregar_bebida("1,Cafe,2,3") == False
    assert agregar_bebida("2,3,Cafe,4") == False
    assert agregar_bebida("4,5,6,7,Cafe") == False
    assert agregar_bebida("8,9,Cafe") == False
 
# 9) Una sola coma separa cada entrada en la lista (válido)
def test_coma_separa_entradas():
    assert agregar_bebida("Espresso,1,2,3") == True
    assert agregar_bebida("Espresso;1,2,3") == False
    assert agregar_bebida("Latte,1,2,3") == True
    assert agregar_bebida("Latte;1;2;3") == False
    assert agregar_bebida("Mocha:1,2,3") == False
    assert agregar_bebida("Espresso-1,2") == False
   # assert agregar_bebida("Cappuccino 1,2,3") == False  # Espacio en vez de coma

# 10) La entrada contiene o no espacios en blanco (válido)
def test_espacios_en_blanco():
    assert agregar_bebida(" Latte , 1 , 2 , 3 ") == True
    assert agregar_bebida("Latte,1,2,3") == True
    assert agregar_bebida(" Espresso,1,2,3 ") == True  # Espacios alrededor
    assert agregar_bebida("Cappuccino , 4 , 5 ") == True  # Espacios entre comas
    assert agregar_bebida(" Latte , 6 , 7,8 ") == True  # Mezcla de espacios
    assert agregar_bebida("Tea,12,13,14") == True  # Sin espacios extra
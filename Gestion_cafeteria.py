def agregar_bebida(entrada):
    # Eliminar espacios en blanco de la entrada
    entrada = entrada.replace(" ", "")
    
    # Dividir la entrada por la coma para separar el nombre de los tamaños
    partes = entrada.split(",")
    
    # Verificar que haya al menos dos partes (nombre y al menos un tamaño)
    if len(partes) < 2:
        return False
    
    # El nombre del artículo debe ser alfabético y tener entre 2 y 15 caracteres
    nombre_articulo = partes[0]
    if not nombre_articulo.isalpha() or not (2 <= len(nombre_articulo) <= 15):
        return False
    
    # Extraer y validar los tamaños
    tamanos = partes[1:]
    
    # Verificar que haya de 1 a 5 tamaños
    if not (1 <= len(tamanos) <= 5):
        return False
    
    # Convertir tamaños a enteros y verificar que estén en el rango de 1 a 48 y en orden ascendente
    tamanos_enteros = []
    ultimo_tamano = 0
    for tamano in tamanos:
        if not tamano.isdigit() or not (1 <= int(tamano) <= 48):
            return False
        tamano_entero = int(tamano)
        if tamano_entero <= ultimo_tamano: # Verificar orden ascendente
            return False
        ultimo_tamano = tamano_entero
        tamanos_enteros.append(tamano_entero)
    
    # Si todos los controles son pasados, la entrada es válida
    return True
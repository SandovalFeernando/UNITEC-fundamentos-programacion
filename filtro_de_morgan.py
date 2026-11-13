# Universo (U): Lista total de registros de calificaciones capturados
registros_calificaciones = [85, -5, 100, None, 105, 0, 72, None, 94]

# 1. Filtro mediante Forma Disyuntiva Negada: -(A v B)
# "Descartar si es nulo O está fuera del rango [0, 100]"
datos_validos_disyuntiva = [c for c in registros_calificaciones if not (c is None or (c < 0 or c > 100))]

# 2. Filtro mediante Forma de Intersección Negada: -A ^ -B
# "Conservar si NO es nulo Y es >=0 Y es <=100"
datos_validos_interseccion = [c for c in registros_calificaciones if (c is not None) and (c >= 0 and c <= 100)]

# Verificación de equivalencia
print("Forma disyuntiva negada: ", datos_validos_disyuntiva)
print("Forma intersección negada: ", datos_validos_interseccion)
print("¿Son idénticos?: ", datos_validos_disyuntiva == datos_validos_interseccion)
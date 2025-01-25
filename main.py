def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(buffer, temp):
    lexemas = []
    i = 0
    while i < len(buffer):
        if buffer[i] == " ":
            lexemas.append("".join(temp))
            temp.clear()
        elif buffer[i] == "eof":
            if temp:
                lexemas.append("".join(temp))
            break
        else:
            temp.append(buffer[i])
        i += 1
    return lexemas, temp

entrada = list("Esto es un ejemplo de entrada con eof")
inicio = 0
tamano_buffer = 10
temp = []

while inicio < len(entrada):
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexemas, temp = procesar_buffer(buffer, temp)
    for lexema in lexemas:
        print(f'Lexema procesado: {lexema}')
    inicio += tamano_buffer
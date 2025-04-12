'''Concatenacion'''

# Concatenar Cadenas de Texto

saludo = "Hola"
nombre = "Francisco"
mensaje = saludo + ", " + nombre
print(mensaje)  # Resultado: Hola, Francisco

# Concatenar usando una cadena formateada con f

print(f"Chatbot: {saludo}, {nombre}!!!")

# Concatenar usando el metodo .format()

nombre = 'Fran'
edad = 33

print("Hola {} tu edad es: {}".format(nombre,edad))
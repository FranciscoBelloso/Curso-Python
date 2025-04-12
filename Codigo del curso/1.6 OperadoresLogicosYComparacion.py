'''Operadores logicos y de comparacion'''

# Operadores de comparacion

a=5
b=2
c=1

igual = a==b
desigualdad = a!=b
mayor_que = a>b
menor_que = a<b
mayor_igual_que = a>=b
menor_igual_que = a<=b
print("Igual: {},desigual: {},mayor que: {},menor que: {},mayor o igual que: {},menor o igual que: {}".format(igual,desigualdad,mayor_que,menor_que,mayor_igual_que,menor_igual_que))

# Operadores Logicos

pregunta = a>b and b>c
pregunta1 = a>b and b<c
pregunta2 = a>b or b<c 
pregunta3 = not a>b

print("Pregunta: {},Pregunta1: {}, Pregunta2: {},Pregunta3: {}".format(pregunta,pregunta1,pregunta2,pregunta3))
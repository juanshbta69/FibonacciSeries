# Definicion de la funcion de calculo
def fibonacci(numero):

    if numero == 1 or numero == 2:
        return 1
    return fibonacci(numero - 1) + fibonacci(numero - 2)

# Ingreso del numero de iteraciones
iteraciones = int(raw_input("Ingrese el numero de iteraciones que desea calcular: "))

# Ciclo para construir la serie de Fibonacci
resultado = []
cont = 1
while cont <= iteraciones:
    resultado.append(fibonacci(cont + 1))
    cont += 1

# Impresion del resultado
print "Serie de Fibonacci: ", resultado
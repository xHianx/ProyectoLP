# Definicion de una funcion que multiplica dos numeros
def multiplicar(a, b)
    a * b
  end
  
  # Definicion de un arreglo con números
  numeros = [2, 4, 6, 8]
  
  # Estructura de control: condicional simple
  if numeros[0] > 1
    puts "El primer numero del arreglo es mayor que 1"
  end
  
  # Llamada a la funcion definida anteriormente
  resultado = multiplicar(numeros[1], numeros[2])
  
  # Impresion del resultado
  puts "El resultado de la multiplicacion es #{resultado}"  
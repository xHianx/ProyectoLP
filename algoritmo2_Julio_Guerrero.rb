# Algoritmo de prueba - algoritmo2.rb

# Definición de variables con diferentes tipos de datos
entero = 42                   # Entero
decimal = 3.14                # Flotante
texto = "Hola, Ruby!"         # Cadena de texto

# Operadores aritméticos
suma = entero + decimal        # Suma
resta = entero - decimal       # Resta
producto = entero * decimal    # Multiplicación
division = entero / decimal    # División
potencia = entero ** 2        # Potencia

# Operadores de comparación
es_igual = entero == decimal   # Igualdad
es_diferente = entero != decimal  # Desigualdad
mayor_que = entero > decimal   # Mayor que
menor_que = entero < decimal   # Menor que
mayor_o_igual = entero >= decimal  # Mayor o igual
menor_o_igual = entero <= decimal  # Menor o igual

# Operadores lógicos
and_logico = (entero > 20) && (decimal < 5)  # AND lógico
or_logico = (entero > 20) || (decimal < 5)   # OR lógico
not_logico = !(entero == decimal)            # NOT lógico

# Imprimir los resultados
puts "Resultado de la suma: #{suma}"
puts "Resultado de la resta: #{resta}"
puts "Resultado de la multiplicación: #{producto}"
puts "Resultado de la división: #{division}"
puts "Resultado de la potencia: #{potencia}"

puts "¿El entero es igual al decimal? #{es_igual}"
puts "¿El entero es diferente al decimal? #{es_diferente}"
puts "¿El entero es mayor que el decimal? #{mayor_que}"
puts "¿El entero es menor que el decimal? #{menor_que}"
puts "¿El entero es mayor o igual al decimal? #{mayor_o_igual}"
puts "¿El entero es menor o igual al decimal? #{menor_o_igual}"

puts "Resultado de AND lógico: #{and_logico}"
puts "Resultado de OR lógico: #{or_logico}"
puts "Resultado de NOT lógico: #{not_logico}"

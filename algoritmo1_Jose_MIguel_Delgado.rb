# Algoritmo de prueba - algoritmo1.rb

# Comentario de una sola línea
def suma(a, b)
  # Este es otro comentario dentro de una función
  return a + b
end

# Uso de operadores aritméticos
resultado = suma(3, 4) * 10 + 5 / 2

# Comentario multilínea
=begin
Este es un comentario
de múltiples líneas.
=end

# Uso de estructuras de control
if resultado > 10
  puts "El resultado es mayor que 10"
else
  puts "El resultado es menor o igual a 10"
end

# Uso de array y hash
arreglo = [1, 2, 3]
hash = { clave: "valor" }

# Comprobación de módulo
resto = 10 % 3

# Salida del resultado
puts "Resultado final: #{resultado}"
puts "Resto de la división: #{resto}"
puts "Array: #{arreglo}"
puts "Hash: #{hash}"

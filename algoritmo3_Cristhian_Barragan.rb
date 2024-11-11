# Algoritmo de prueba - algoritmo3.rb

# Palabras reservadas y su uso
if true
  puts "Esto es una sentencia if"
elsif false
  puts "Esto no se ejecuta"
else
  puts "Esto se ejecuta porque la condición es falsa"
end

# Uso de 'while' para un bucle
counter = 0
while counter < 5
  puts "Contador: #{counter}"
  counter += 1
end

# Definición de un método con 'def' y 'end'
def saludo(nombre)
  puts "Hola, #{nombre}!"
end

# Llamando al método
saludo("Josemiu")

# Definición de variables
# Variables locales
variable_local = "Soy una variable local"
puts variable_local

# Variables globales
$variable_global = "Soy una variable global"
puts $variable_global

# Variables de instancia
@variable_instancia = "Soy una variable de instancia"
puts @variable_instancia

# Variables de clase
@@variable_clase = "Soy una variable de clase"
puts @@variable_clase

# Uso de 'return' en un método
def multiplicar(a, b)
  return a * b
end
resultado = multiplicar(4, 5)
puts "Resultado de la multiplicación: #{resultado}"

# Uso de 'self' para acceder al objeto actual
class MiClase
  def mostrar_self
    puts self
  end
end

obj = MiClase.new
obj.mostrar_self

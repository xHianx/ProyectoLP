variable="hola, como estas"
variable.to_f
$global_var = "Es una variable global"

# Variable de clase 
@personas = 0 
 
# Constructor 
def initialize(nombre, edad) 
  @nombre = nombre      # Variable deinstancia 
  @edad = edad          # Variable de instancia 
  @personas += 1 # Incrementa el contador de personas 
end 
 
# Método de instancia 
def presentarse 
  puts "Hola, me llamo #{@nombre} y mi edad #{@edad}." 
end 
 
# Método de clase 
def self.personas 
  @personas 
end 

def initialize(nombre, edad, grado) 
  super(nombre, edad)   # Llama al constructor de la clase base 
  @grado = grado        # Variable de instancia 
end 
 
  # Sobreescribe el método presentarse 
def presentarse 
  super() 
  puts "Estoy en el grado @grado" 
end 
 
# Función para pedir datos por teclado 
def pedir_datos(mensaje) 
  print mensaje 
  gets.chomp 
end 
 
# Programa principal 
puts $global_var 
 
# Pedir nombre y edad 
nombre = pedir_datos("Por favor, ingresa tu nombre: ") 
edad = pedir_datos("Por favor, ingresa tu edad: ").to_i 
 
# Crear instancia de Persona 
persona = Persona.new(nombre, edad) 
persona.presentarse 
 
# Pedir grado y crear instancia de Estudiante 
grado = pedir_datos("Por favor, ingresa tu grado: ") 
estudiante = Estudiante.new(nombre, edad, grado) 
estudiante.presentarse 
 
# Comparaciones lógicas 
puts "Eres mayor de edad" if edad >= 18 
 
# Diccionario (Hash) con símbolos 
informacion = { 
  nombre=> nombre, 
  edad=> edad, 
  grado=> grado 
} 
 
puts "Información: #{@informacion}" 
 
# Array 
numeros = [1, 2, 3, 4, 5] 
test = "este es un test"
 
# Iterar sobre el array con `each` 
numeros.each do |num| 
  puts "Numero: num" 
end 
 
# Operaciones aritméticas 
promedio = suma.to_f / numeros.size 
 
puts "Suma: #{@suma}, Promedio: #{@promedio}"
test.to_f 
 
# Caso `case` 
valor = pedir_datos("Ingresa un número del 1 al 3: ").to_i 
 
case valor 
when 1 
  puts "Elegiste uno" 
when 2 
  puts "Elegiste dos" 
when 3 
  puts "Elegiste tres" 
else 
  puts "Valor fuera del rango" 
end 
 
# Booleanos y operaciones 
boo1 = true 
boo2 = false 
 
if boo1 && !boo2 
  puts "Boo1 es verdadero y Boo2 es falso" 
end 
 
puts "Total de personas: personas"
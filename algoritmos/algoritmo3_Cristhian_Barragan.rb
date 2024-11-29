# Definición de una clase con métodos y atributos 
class Vehiculo 
  attr_accessor :marca, :modelo, :velocidad 
  def initialize(marca, modelo, velocidad = 
  0) 
      @marca = marca 
      @modelo = modelo 
      @velocidad = velocidad 
  end 
  
  def acelerar(incremento) 
      @velocidad += incremento 
  end 
  
  def frenar(decremento) 
      @velocidad -= decremento 
      @velocidad = 0 if @velocidad < 0 
  end 
  
  def estado 
      "El #{@marca} #{@modelo} va a #{@velocidad} km/h." 
  end 
  end 
  
# Creación de un objeto 
vehiculo1 = Vehiculo.new("Toyota", "Corolla") 
puts vehiculo1.estado 
  
# Uso de un array 
marcas = ["Ford", "Chevrolet", "Honda"] 
marcas << vehiculo1.marca 
  
# Uso de un diccionario (hash) 
modelos = { "Ford" => "Focus", "Chevrolet" => "Malibu", "Honda" => "Civic" } 
  modelos[vehiculo1.marca] = vehiculo1.modelo 
  
# Ciclo for 
  puts "Marcas en la lista:" 
  for marca in marcas 
  puts marca 
  end 
  
# Ciclo while 
  contador = 0 
  while contador < marcas.length 
  puts "Marca #{contador + 1}: 
  #{marcas[contador]}" 
  contador += 1 
  end 
  
# Condicionales y expresiones booleanas 
  puts "Condicionales y expresiones 
  booleanas:" 
  marcas.each do |marca| 
  if modelos[marca] 
      puts "El modelo de #{marca} es #{modelos[marca]}." 
  else 
      puts "Modelo no registrado para #{marca}." 
  end 
  end 
  
# Uso de case 
  puts "Uso de case:" 
  marcas.each do |marca| 
  case modelos[marca] 
  when "Focus" 
      puts "#{marca} tiene el modelo Focus." 
  when "Malibu" 
      puts "#{marca} tiene el modelo Malibu." 
  when "Civic" 
      puts "#{marca} tiene el modelo Civic." 
  when vehiculo1.modelo 
      puts "#{marca} tiene el modelo #{vehiculo1.modelo}." 
  else 
      puts "Modelo desconocido para #{marca}." 
  end 
  end 
  
# Expresiones aritméticas 
  puts "Expresiones aritméticas:" 
  vehiculo1.acelerar(50) 
  vehiculo1.frenar(20) 
  puts vehiculo1.estado 
  
# Expresiones booleanas y operaciones con  arrays 
  puts "Operaciones con arrays y expresiones booleanas:" 
  marcas_duplicadas = ["Ford", "Chevrolet", 
  "Honda", "Toyota", "Ford"] 
  marcas_unicas = marcas_duplicadas.uniq 
  puts "Marcas únicas: #{marcas_unicas.join(', ')}" 
  
# Uso de un método con parámetros y valores de retorno 
  def calcular_factorial(n) 
  return 1 if n <= 1 
  n * calcular_factorial(n - 1) 
  end 
  
  puts "Factorial de 5 es: #{calcular_factorial(5)}
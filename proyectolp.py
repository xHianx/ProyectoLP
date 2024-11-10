import ply.lex as lex
import datetime

# Palabras reservadas en Ruby
# Aporte de Cristhian
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'unless': 'UNLESS',
    'case': 'CASE',
    'when': 'WHEN',
    'while': 'WHILE',
    'until': 'UNTIL',
    'for': 'FOR',
    'break': 'BREAK',
    'next': 'NEXT',
    'redo': 'REDO',
    'retry': 'RETRY',
    'def': 'DEF',
    'class': 'CLASS',
    'module': 'MODULE',
    'end': 'END',
    'self': 'SELF',
    'yield': 'YIELD',
    'return': 'RETURN',
    'super': 'SUPER',
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NIL',
    'begin': 'BEGIN',
    'rescue': 'RESCUE',
    'ensure': 'ENSURE',
    'do': 'DO',
    'in': 'IN',
    'alias': 'ALIAS',
    'defined?': 'DEFINED'
}

# Definición de los tokens
tokens = (
    'SINGLE_LINE_COMMENT',   # Comentarios de una línea
    'MULTI_LINE_COMMENT',    # Comentarios de múltiples líneas
    'LPAREN',                # Paréntesis izquierdo '('
    'RPAREN',                # Paréntesis derecho ')'
    'LBRACKET',              # Corchete izquierdo '['
    'RBRACKET',              # Corchete derecho ']'
    'LBRACE',                # Llave izquierda '{'
    'RBRACE',                # Llave derecha '}'
    'COMMA',                 # Coma ','
    'SEMICOLON',             # Punto y coma ';'
    'INTEGER',               # Enteros '42'
    'FLOAT',                 # Flotantes '3.14'
    'STRING',                # Strings "texto"
    'VARIABLE_LOCAL',        # Variables locales
    'VARIABLE_GLOBAL',       # Variables globales
    'VARIABLE_INSTANCIA',    # Variables de instancia
    'VARIABLE_CLASE',        # Variables de clase
) + tuple(reserved.values())

# Expresiones regulares para los delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

# Expresiones regulares para los comentarios
t_SINGLE_LINE_COMMENT = r'\#.*'  # Comentarios de una sola línea (empieza con '#')
t_MULTI_LINE_COMMENT = r'=begin.*?=end'  # Comentarios multilínea (deben empezar con '=begin' y terminar con '=end')

### JULIO GUERRERO
# Expresiones regulares para los tipos de datos
def t_INTEGER(t):
    r'(-\d|\d)\d*'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'(-\d|\d)\d*\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\"([^\"\\]|\\.)*\"'
    t.value = str(t.value)
    return t

# Aporte de Cristhian: Expresiones regulares para variables en Ruby
t_VARIABLE_LOCAL = r'[a-z_][a-zA-Z0-9_]*'
t_VARIABLE_GLOBAL = r'\$[a-zA-Z_][a-zA-Z0-9_]*'
t_VARIABLE_INSTANCIA = r'@[a-zA-Z_][a-zA-Z0-9_]*'
t_VARIABLE_CLASE = r'@@[a-zA-Z_][a-zA-Z0-9_]*'

# Aporte de Cristhian: Regla para palabras reservadas en Ruby
def t_RESERVED(t):
    r'\b(if|else|elsif|unless|case|when|while|until|for|break|next|redo|retry|def|class|module|end|self|yield|return|super|true|false|nil|begin|rescue|ensure|do|in|alias|defined\?)\b'
    t.type = reserved.get(t.value, 'ID')  # Cambia el tipo de token si es una palabra reservada
    return t

# Definir una regla para contar las líneas y manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definir los caracteres que deben ser ignorados (espacios y tabulaciones)
t_ignore = ' \t'

### JULIO GUERRERO
# Manejo de caracteres ilegales
def t_error(t):
    f.write(f"Caracter ilegal: {t.value[0]}\n")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Ejemplo de código Ruby con comentarios y delimitadores
data = '''
# Esto es un comentario de una línea
def suma(a, b)
  # Este es otro comentario
  @instancia_var = 10
  @@clase_var = 20.5
  $global_var = "valor global"
  variable_local = 30
  if true
    for i in [1, 2, 3]
      puts "Número: #{i}"
    end
  else
    puts "No hay números"
  end
end

=begin
Este es un comentario de múltiples líneas.
Puede ocupar varias líneas.
=end

puts suma(3, 4)
'''

# Darle al lexer el código de entrada
lexer.input(data)

### JULIO GUERRERO
# Tokenizar y mostrar los tokens
FECHA = datetime.datetime.now().date()
HORA = datetime.datetime.now().hour
MINUTO = datetime.datetime.now().minute

nombre_archivo = f"logs/lexico-{FECHA}-{HORA}-{MINUTO}.txt".replace(":", "-")

with open(nombre_archivo, "a", encoding="utf-8") as f:
    while True:
        tok = lexer.token()
        if not tok:
            break  # No hay más entradas
        f.write(f"Tipo: {tok.type}, Valor: {tok.value}\n")

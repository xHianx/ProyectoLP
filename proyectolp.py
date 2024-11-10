import ply.lex as lex
import datetime

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
    'ARRAY',                 # Array '[1, 2, 3]'
    'HASH',                  # Hashes '{clave: "valor"}'
    'PLUS',                  # Suma '+'
    'MINUS',                 # Resta '-'
    'TIMES',                 # Multiplicacion '*'
    'DIVIDE',                # Division '/'
    'POWER',                 # Potencia '/'
    'AND',                   # Y '&&'
    'OR',                    # O '||'
    'NOT',                   # Nengacion '!'
    'EQUAL',                 # Igualdad '=='
    'NOTEQUAL',              # Desigualdad '--'
    'BIGGER',                # Mayor que '>'
    'SMALLER',               # Menor que '<'
    'BIGGEREQUAL',           # Mayor o igual '>='
    'SMALLEREQUAL',          # # Menor o igual '<='
    'ASSIGNATION',           # Asignacion '='
    'INCREMENT',             # Incremento '+='
    'DECREMENT',             # Decremento '-='

)

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
def t_FLOAT(t):
    r'(-\d|\d)\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'(-\d|\d)\d*'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\"\\]|\\.)*\"'
    t.value = str(t.value)
    return t

t_ARRAY = r'\[\s*(?:[^\]]+\s*(?:,\s*[^\]]+\s*)*)?\]' 

t_HASH = r'\{\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*".*"\s*\}'

## JULIO GUERRERO
# Expresiones regulares para operadores
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER   = r'\*\*'

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_BIGGER = r'>'
t_SMALLER = r'<'
t_BIGGEREQUAL = r'>='
t_SMALLEREQUAL = r'<='
t_ASSIGNATION = r'='
t_INCREMENT = r'\+='
t_DECREMENT = r'-='

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
  return a + b
end

=begin
Este es un comentario de múltiples líneas.
Puede ocupar varias líneas.
=end

puts suma(3, 4)

"texto aqui"
42
3.14
[1, 2, 3]
{clave: "valor"}

true
false
nil

+=-*/%**
&&||!
==!=><>=<=
=+=-=
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

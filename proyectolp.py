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

# Expresiones regulares con alguna acción de código
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

# Definir una regla para contar las líneas y manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definir los caracteres que deben ser ignorados (espacios y tabulaciones)
t_ignore = ' \t'

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

cadena = "texto aqui"

'''

# Darle al lexer el código de entrada
lexer.input(data)

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

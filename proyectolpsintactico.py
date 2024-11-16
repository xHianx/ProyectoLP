import ply.lex as lex
import ply.yacc as yacc
import os

# Crear directorio de logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Palabras reservadas en Ruby
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
    'defined?': 'DEFINED',
    'puts': 'PUTS'
}

# Lista de tokens
tokens = [
    # Comentarios
    'SINGLE_LINE_COMMENT',   # Comentarios de una sola línea
    'MULTI_LINE_COMMENT',    # Comentarios de varias líneas

    # Delimitadores
    'LPAREN',                # Paréntesis izquierdo '('
    'RPAREN',                # Paréntesis derecho ')'
    'LBRACKET',              # Corchete izquierdo '['
    'RBRACKET',              # Corchete derecho ']'
    'LBRACE',                # Llave izquierda '{'
    'RBRACE',                # Llave derecha '}'
    'COMMA',                 # Coma ','
    'SEMICOLON',             # Punto y coma ';'

    # Literales
    'INTEGER',               # Números enteros (por ejemplo: '42')
    'FLOAT',                 # Números flotantes (por ejemplo: '3.14')
    'STRING',                # Cadenas de texto (por ejemplo: "hola")
    'ARRAY',                 # Arreglos (por ejemplo: '[1, 2, 3]')
    'HASH',                  # Hashes (por ejemplo: '{clave: "valor"}')

    # Operadores
    'PLUS',                  # Operador de suma '+'
    'MINUS',                 # Operador de resta '-'
    'TIMES',                 # Operador de multiplicación '*'
    'DIVIDE',                # Operador de división '/'
    'POWER',                 # Operador de potencia '**'
    'AND',                   # Operador lógico "y" '&&'
    'OR',                    # Operador lógico "o" '||'
    'NOT',                   # Operador lógico de negación '!'
    'EQUAL',                 # Operador de igualdad '=='
    'NOTEQUAL',              # Operador de desigualdad '!='
    'BIGGER',                # Operador mayor que '>'
    'SMALLER',               # Operador menor que '<'
    'BIGGEREQUAL',           # Operador mayor o igual que '>='
    'SMALLEREQUAL',          # Operador menor o igual que '<='
    'ASSIGNATION',           # Operador de asignación '='
    'INCREMENT',             # Operador de incremento '+='
    'DECREMENT',             # Operador de decremento '-='

    # Variables
    'VARIABLE_LOCAL',        # Variables locales
    'VARIABLE_GLOBAL',       # Variables globales
    'VARIABLE_INSTANCIA',    # Variables de instancia
    'VARIABLE_CLASE',        # Variables de clase
] + list(reserved.values())  # Añadir las palabras reservadas

# Reglas de expresiones regulares para los tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGNATION = r'='
t_BIGGER = r'>'

# Definir reglas específicas
def t_STRING(t):
    r'"[^"]*"'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t

# Ignorar espacios en blanco y comentarios
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Reglas sintácticas
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                     | statement statement_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : function_def
                | assignment
                | if_statement
                | puts_statement
                | expression'''
    p[0] = p[1]

def p_function_def(p):
    '''function_def : DEF VARIABLE_LOCAL LPAREN param_list RPAREN expression END'''
    p[0] = ('function_def', p[2], p[4], p[6])

def p_param_list(p):
    '''param_list : VARIABLE_LOCAL COMMA VARIABLE_LOCAL
                 | VARIABLE_LOCAL
                 | empty'''
    if len(p) == 4:
        p[0] = [p[1], p[3]]
    else:
        p[0] = [p[1]] if p[1] else []

def p_assignment(p):
    '''assignment : VARIABLE_LOCAL ASSIGNATION expression'''
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF expression statement_list END'''
    p[0] = ('if', p[2], p[3])

def p_puts_statement(p):
    '''puts_statement : PUTS expression'''
    p[0] = ('puts', p[2])

def p_expression(p):
    '''expression : INTEGER
                 | STRING
                 | VARIABLE_LOCAL
                 | array
                 | array_access
                 | function_call
                 | binary_operation'''
    p[0] = p[1]

def p_array(p):
    '''array : LBRACKET array_elements RBRACKET'''
    p[0] = ('array', p[2])

def p_array_elements(p):
    '''array_elements : INTEGER
                     | INTEGER COMMA array_elements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_array_access(p):
    '''array_access : VARIABLE_LOCAL LBRACKET INTEGER RBRACKET'''
    p[0] = ('array_access', p[1], p[3])

def p_function_call(p):
    '''function_call : VARIABLE_LOCAL LPAREN arg_list RPAREN'''
    p[0] = ('function_call', p[1], p[3])

def p_arg_list(p):
    '''arg_list : expression
                | expression COMMA arg_list
                | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = [p[1]] + p[3]

def p_binary_operation(p):
    '''binary_operation : expression TIMES expression
                       | expression BIGGER expression'''
    p[0] = ('binary_op', p[2], p[1], p[3])

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Error de sintaxis: {p.type} ('{p.value}') en la línea {p.lineno}")
    else:
        print("Error de sintaxis: Fin de archivo inesperado")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Análisis del archivo Ruby
file_path = "C:/Users/José Miguel/ProyectoLP/algoritmodeprueba_Jose_Miguel_Delgado.rb"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()
except FileNotFoundError:
    print(f"Error: Archivo '{file_path}' no encontrado.")
    exit(1)

result = parser.parse(code)
print(result)

import ply.yacc as yacc
from proyectolp import tokens
from nombresarchivos import file_path_read, file_path_write_sint

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'AND', 'OR'),  # Añadido por Cristhian: Soporte para operadores lógicos
    ('right', 'NOT'),       # Añadido por Cristhian: Soporte para negación lógica
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
                | while_statement  # Añadido por Cristhian: Soporte para bucles while
                | puts_statement
                | gets_statement  # Añadido por Cristhian: Soporte para solicitud de datos
                | expression'''
    p[0] = p[1]

def p_variable(p):
    '''variable : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_INSTANCIA
                | VARIABLE_CLASE'''
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
    '''assignment : variable ASSIGNATION expression'''
    p[0] = ('assignment', p[1], p[3])

# Estructuras de control (nueva regla añadida por Cristhian)
def p_while_statement(p):
    '''while_statement : WHILE expression DO statement_list END'''
    p[0] = ('while', p[2], p[4])

def p_if_statement(p):
    '''if_statement : IF expression statement_list END'''
    p[0] = ('if', p[2], p[3])

## JULIO GUERRERO
def p_puts_statement(p):
    '''puts_statement : PUTS arg_list'''
    p[0] = ('puts', p[2])

# Añadido por Cristhian: Soporte para solicitud de datos
def p_gets_statement(p):
    '''gets_statement : VARIABLE_LOCAL ASSIGNATION GETS'''
    p[0] = ('gets', p[1])

# Expresiones booleanas añadidas por Cristhian
def p_expression_boolean(p):
    '''expression : expression AND expression
                  | expression OR expression
                  | NOT expression'''
    if len(p) == 3:
        p[0] = ('not', p[2])
    else:
        p[0] = (p[2], p[1], p[3])

## JULIO GUERRERO 
def p_expression(p):
    '''expression : INTEGER
                 | STRING
                 | variable
                 | array
                 | array_access
                 | function_call
                 | binary_operation
                 | GETS
                 | hash'''
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

def p_hash(p):
    '''hash : LBRACE hash_elements RBRACE'''
    p[0] = ('hash', p[2])

def p_hash_elements(p):
    '''hash_elements : hash_element
                     | hash_element COMMA hash_elements
                     | empty'''
    if len(p) == 2:
        if p[1] is None:
            p[0] = {}
        else:
            p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {p[1][0]: p[1][1]}
        p[0].update(p[3])

def p_hash_element(p):
    '''hash_element : VARIABLE_LOCAL COLON STRING'''
    p[0] = (p[1], p[3])

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

## JULIO GUERRERO 
# Proceso de análisis
def analyze_file(file_path_r, file_path_w):
    try:
        with open(file_path_r, "r", encoding="utf-8") as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path_r}' no encontrado.")
        return

    result = parser.parse(code)
    
    try:
        with open(file_path_w, "a", encoding="utf-8") as log:
            log.write(str(result))
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path_w}' no encontrado.")
        return


analyze_file(file_path_read, file_path_write_sint)

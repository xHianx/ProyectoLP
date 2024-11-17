import ply.yacc as yacc
from proyectolp import tokens
from nombresarchivos import file_path_read, file_path_write

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


analyze_file(file_path_read, file_path_write)

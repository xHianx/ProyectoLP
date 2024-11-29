import ply.lex as lex

#escritura_a_carpeta_log
import datetime
ruta_carpeta="logs"
ruta_algoritmos="algoritmos"
noReconocidos=[]

# Palabras reservadas en Ruby
# Aporte de Cristhian Barragan
reserved = {
    "true":"TRUE",
    "false":"FALSE",
    "or":"OR",
    "not":"NOT",
    "if":"IF",
    "return":"RETURN",
    "class":"CLASS",
    "module":"MODULE",
    "self":"SELF",
    "begin":"BEGIN",
    "else":"ELSE",
    "while":"WHILE",
    "and":"AND",
    #Julio Guerrero
    "in": "IN",
    "case": "CASE",
    "def": "DEF",
    "end": "END",
    "return": "RETURN",
    "printf": "PRINTF",
    "to_f": "TO_F",
    "concat": "CONCAT",
    "initialize" : "INITIALIZE",
    "gets": "GETS",
    "chomp": "CHOMP",
    "each":"EACH",
    "elsif": "ELSEIF",
    "until":"UNTIL",
    "for": "FOR",
    "sort": "SORT",
    "puts": "PUTS",
    "print": "PRINT",
    "do": "DO",
    "when" : "WHEN",
}


# Definición de los tokens 
tokens=[
    #Julio Guerrero
    'ID_CLASE',
    'TRES_PUNTOS',
    'PUNTO',
    'VARIABLECLASE',
    'VARIABLE',
    'CADENA',

    #Cristhian Barragan
    'FLOTANTE',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'MODULO',
    'PARENTESIS_IZ',
    'PARENTESIS_DER',
    'IGUAL_DOBLEP',
    'DOBLE_IGUAL',
    'IGUAL',
    'COMA',
    'O_SIGNO',
    'Y_SIGNO',
    'NAVE',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_IGUAL_QUE',
    'EXCLAMACION_BAJO',
    'EXCLAMACION_ALTO',
    'DIFERENTE',
    'COMENTARIO',
    'COMENTARIO_MULTI',
   
    #Jose Delgado
    'SIMBOLO',
    'COMILLA_S',
    'COMILLA_D',
    'LLAVE_IZ',
    'LLAVE_DER',
    'PORCENTAJE',
    'BARRA',
    'MULTIPLICACION',
    'EXPONENCIACION',
    'CORCHETE_IZ',
    'CORCHETE_DER',
    'TRIPLE_IGUAL',
    'ASIGNA_HASH',
    'PREGUNTA'
    
]+list(reserved.values())

# Expresiones regulares

#Para los tokens 
#Cadenas
#Jose Delgado
t_TRES_PUNTOS =r'\.\.\.'
t_PUNTO =r'\.'
t_NAVE =r'<=>'

#Flotantes 
def t_FLOTANTE(t):
    r'[-]?(0|[1-9]\d*)+\.{1}\d*'
    t.value=float(t.value)
    return t 

#Enteros
def t_ENTERO(t):
    r'[-]?[0-9]+'
    t.value=int(t.value)
    return t 

#Operadores y Delimitadores

#Cristhian Barragan
t_Y_SIGNO=r'&&'
t_COMA=r','
t_O_SIGNO=r'\|\|'
t_PARENTESIS_IZ= r'\('
t_PARENTESIS_DER= r'\)'
t_MAYOR_IGUAL_QUE=r'>='
t_MENOR_IGUAL_QUE=r'<='
t_MAYOR_QUE=r'>'
t_MENOR_QUE=r'<'
t_EXCLAMACION_BAJO=r'!'
t_EXCLAMACION_ALTO=r'¡'
t_IGUAL=r'='
t_DIFERENTE=r'!='
t_IGUAL_DOBLEP=r'=='
t_MAS= r'\+'
t_MODULO= r'%'
t_MENOS= r'-'
t_DIVISION= r'/'
#Julio Guerrero
t_MULTIPLICACION=r'\*'
t_COMILLA_D=r'\"'
t_COMILLA_S=r'\''
t_LLAVE_DER=r'}'
t_LLAVE_IZ=r'{'
t_PORCENTAJE=r'%'
t_BARRA=r'\|'
t_EXPONENCIACION=r'\*\*'
t_CORCHETE_IZ=r'\['
t_CORCHETE_DER=r'\]'
t_TRIPLE_IGUAL=r'==='
t_ASIGNA_HASH=r'=>'
t_PREGUNTA=r'\?'

#simbolos 
def t_SIMBOLO(t):
    r':[a-zA-Z_][a-zA-Z0-9_]*'
    return t

#variables
def t_ID_CLASE(t):
    r'[A-Z]{1}[a-z]+'
    return t

#Todos: Julio Guerrero, Jose Delgado y Cristhian Barragan
def t_VARIABLECLASE(t):
    r'[$@]{2}[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@"), 'VARIABLECLASE')
    return t

def t_VARIABLE(t):
    r'[$@]?[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@$"), 'VARIABLE')
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.type = reserved.get(t.value, 'CADENA')
    return t

def t_COMENTARIO(t):
    r'\#.*'
    # t.value = t.value[1:].strip()  
    # return t
    pass

#Comentario multilínea - Detecta el inicio de un comentario multilínea
def t_COMENTARIO_MULTI(t):
    r'=begin(?!.*(?:=begin[\s\S]*?=end))[\s\S]*?=end'
    # return t
    pass

#Poder ignorar espacios
t_ignore = ' \t\r'

#Define una regla para que podamos rastrear los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Como manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    noReconocidos.append(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

#lexer.input('''$global_var = "Es una variable global" ''')

'''
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
'''

def log_function(lexer_instance, algoritmo_file, log_prefix):
    string = ""
    archivo = f"{ruta_algoritmos}/{algoritmo_file}"
    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%Y%m%d-%H%M%S") 
    nombre_archivo = f"{log_prefix}-{fecha_hora}.txt"
    
    with open(archivo, 'r') as f:
        contenido = f.read().strip()
        lexer_instance.input(contenido)
    
    ruta_archivo = f"{ruta_carpeta}/{nombre_archivo}"
    
    while True:
        tok = lexer_instance.token()
        if not tok:
            break
        tipo = tok.type
        valor = tok.value
        valor_str = valor if isinstance(valor, str) else str(valor)
        string = f"Token: tipo={tipo}, valor='{valor_str}'"
        with open(ruta_archivo, "a+") as archivo_log:
            archivo_log.write(string + '\n')
    print(f"Resultado guardado en {ruta_archivo}")

def pruebas_Cristhian():
    lexer_Cristhian = lex.lex()
    log_function(lexer_Cristhian, "algoritmo3_Cristhian_Barragan.rb", "lexico-CristhianBarragan")

def pruebas_Julio():
    lexer_Julio = lex.lex()
    log_function(lexer_Julio, "algoritmo2_Julio_Guerrero.rb", "lexico-JulioGuerrero")

def pruebas_Jose():
    lexer_Jose = lex.lex()
    log_function(lexer_Jose, "algoritmo1_Jose_MIguel_Delgado.rb", "lexico-JoseDelgado")

#tests
pruebas_Cristhian()
pruebas_Julio()
pruebas_Jose()

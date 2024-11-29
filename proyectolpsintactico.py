import ply.yacc as yacc
from lplexico import tokens
from lplexico import lex
import lplexico as l
import datetime

tabla_variables = {}
errors = []
errores_semanticos = []
ruta_carpeta = "logs"
ruta_algoritmos = "algoritmos"
globalFound=False

# Reglas sintácticas
def p_instruccion(p):
      '''instruccion : cuerpoInstruccion'''

def p_cuerpoInstruccion(p):
      '''cuerpoInstruccion : cuerpo
                        | cuerpo cuerpoInstruccion'''
def p_cuerpo(p):
    '''cuerpo : operacionAritmetica
              | input_concatenacion
              | asignacion
              | impresion
              | impresion_vacia
              | expresiones_booleanas
              | solicitudDatosTeclado
              | hashes
              | estructura_ifUnaLinea
              | estructura_if
              | funciones
              | funcionesEstructuras
              | array
              | each_array
              | each_hash
              | sentencia_while
              | sentencia_while_bool
              | sentencia_case
              | sentencias_when
              | sentencia_until
              | definicion_clase
              | entero_a_flotante
              | declaracion'''

#Operaciones
#Cristhian Barragan----comparacion de simbolos 
def p_valorSimbolo(p):
    """valorSimbolo : SIMBOLO 
                    | VARIABLE"""
    valor = p[1]
    
    # Verificar el tipo de token usando p.slice
    if p.slice[1].type == 'SIMBOLO':
        p[0] = valor
    elif p.slice[1].type == 'VARIABLE':
        if valor not in tabla_variables:
            error = f"Error semántico: variable '{valor}' no inicializada"
            errores_semanticos.append(error)
            print(error)
        else:
            valor_variable = tabla_variables[valor]
            if not valor_variable.startswith(":"):
                error = f"Error semántico: variable '{valor}' no es un símbolo"
                errores_semanticos.append(error)
                print(error)
            else:
                p[0] = valor_variable
    else:
        error = f"Error semántico: variable '{valor}' no es de tipo símbolo"
        errores_semanticos.append(error)
        print(error)
        p[0]=None

#Cristhian Barragan----concatenacion de cadenas
def p_input_concatenacion(p):
    """ input_concatenacion : concatenacionSimpleCadena
                            | concatenacion_funcion """
    p[0] = p[1]

def p_concatenacion_funcion(p):
    """ concatenacion_funcion : VARIABLE PUNTO CONCAT PARENTESIS_IZ valorCadena PARENTESIS_DER """
    valor=p[1]
    if valor not in tabla_variables:
        error = f"Error semántico, variable {valor} no ha sido inicializada"
        errores_semanticos.append(error)
        print(error)
        p[0] = None
    else:
        tabla_variables[valor] = tabla_variables[valor] + " " + p[5]
        p[0] = tabla_variables[valor]

def p_valorCadena(p):
    """ valorCadena : CADENA
                    | VARIABLE """
    
    valor=p[1]
     # Verificar si es una cadena directamente
    if p.slice[1].type == 'CADENA':
        p[0] = valor
    # Si es una variable, verificar si está inicializada
    elif p.slice[1].type == 'VARIABLE':
        if valor in tabla_variables:
            # Tiene que ser de tipo string
            if isinstance(tabla_variables[valor], str):
                p[0] = tabla_variables[valor]
            elif isinstance(tabla_variables[valor], float):
                p[0] = tabla_variables[valor]
            else:
                error = f"Error semántico, variable {valor} no es de tipo string"
                errores_semanticos.append(error)
                print(error)
                p[0] = None

        else:
            error = f"Error semántico, variable {valor} no ha sido inicializada"
            errores_semanticos.append(error)
            print(error)
            p[0] = None

    else:
        error = f"Error semántico inesperado con el valor: {valor}"
        errores_semanticos.append(error)
        print(error)
        p[0] = None

def p_concatenacionSimpleCadena(p):
    """concatenacionSimpleCadena : valorCadena MAS valorCadena
                                 | concatenacionSimpleCadena MAS valorCadena"""
    operando1 = p[1]
    operando2 = p[3]
    if (operando1 != None and operando2 != None):
        if (isinstance(operando1, str) and isinstance(operando2, str)):
            p[0] = operando1 + " " + operando2
        else:
            error = f"Error semántico, una de las variables no es de tipo string"
            errores_semanticos.append(error)
            print(error)
    elif operando1 == None:
        p[0] = operando2
    elif operando2 == None:
        p[0] = operando1
    print(p[0])

#Cristhian Barragan
def p_valorNumerico(p):
    """valorNumerico : FLOTANTE 
                     | ENTERO"""

    #Julio Guerrero
    if p.slice[1].type == 'FLOTANTE':
        p[0] = float(p[1])
    elif p.slice[1].type == 'ENTERO':
        p[0] = int(p[1])
    else:
        p[0] = p[1]

def p_soloEnteros(p):
    """soloEnteros : ENTERO"""
    p[0] = int(p[1])

def p_entero_a_flotante(p):
    """entero_a_flotante : VARIABLE PUNTO TO_F"""

    if p[1] in tabla_variables:
        value = tabla_variables[p[1]]
        if isinstance(value, int):
            p[0] = float(value)
        else:
            print(f"Error semántico: '{p[1]}' no es un entero")
            errores_semanticos.append(f"Error semántico: '{p[1]}' no es un entero")
            p[0] = value
    else:
        print(f"Error semántico: Variable '{p[1]}' no definida")
        errores_semanticos.append(f"Error semántico: Variable '{p[1]}' no definida")
        p[0] = 0

def p_operadores(p):
    """operadores : MAS 
                  | MENOS
                  | DIVISION
                  | MULTIPLICACION
                  | EXPONENCIACION 
                  | MODULO"""
    p[0] = p[1]

def p_expresionNumerica(p):
    """expresionNumerica : valorNumerico
                         | operacionAritmetica
                         | PARENTESIS_IZ operacionAritmetica PARENTESIS_DER
                         | VARIABLE"""

    #Jose Delgado
    if p.slice[1].type == 'valorNumerico':
        p[0] = p[1]
    elif p.slice[1].type == 'VARIABLE':
        if p[1] not in tabla_variables:
            print(f"Error semántico: Variable '{p[1]}' no definida")
            errores_semanticos.append(f"Error semántico: Variable no inicializada '{p[1]}'")
        else:
            p[0] = p[1]

def p_operacionAritmetica(p):
    """operacionAritmetica : expresionNumerica operadores expresionNumerica"""
    #Julio Guerrero
    if isinstance(p[1],str) or isinstance(p[3], str):
        for i in tabla_variables:
            if i[0] == p[1]:
                if not isinstance(tabla_variables[p[1]], float) and not isinstance(tabla_variables[p[1]], int): 
                    print(f"Error semántico: '{p[1]}' no es un valor numérico")
                    errores_semanticos.append(f"Error semántico: '{p[1]}' no es un valor numérico")
                else:
                    pass
            elif i[0] == p[3]:
                if not isinstance(tabla_variables[p[3]], float) and not isinstance(tabla_variables[p[3]], int): 
                    print(f"Error semántico: '{p[3]}' no es un valor numérico")
                    errores_semanticos.append(f"Error semántico: '{p[3]}' no es un valor numérico")
                else:
                    pass
            else:
                pass

#AGREGAR CON PUTS Y + DE 1 ARGUMENTO Cristhian Barragan
def p_valor_print(p):
    """valor_print : PRINT
                   | PUTS """
    
def p_valores(p):
    """valores : valor
               | valor COMA valores
               | valor estructura_ifUnaLinea
               | valor sentencia_while_bool"""
    
#Cristhian Barragan
def p_booleanos(p):
    """booleanos : TRUE
                | FALSE"""
    if p[1] == 'True':
        p[0] = True
    else:
        p[0] = False

def p_valor(p):
    """valor : CADENA
             | valorNumerico
             | VARIABLE
             | VARIABLECLASE
             | SIMBOLO"""

    if p.slice[1].type == 'VARIABLE':
        if p[1] in tabla_variables:
            p[0] = tabla_variables[p[1]]
        else:
            error = f"Error semántico, variable {p[1]} no ha sido inicializada"
            errores_semanticos.append(error)
            print(error)
            p[0] = None
    elif p.slice[1].type == 'CADENA':
        p[0] = p[1]
    elif p.slice[1].type == 'valorNumerico':
        p[0] = p[1]
    else:
        p[0] = p[1]

def p_impresion(p):
    """impresion : valor_print valores"""

def p_asignacion_clase(p):
    '''asignacion_clase : VARIABLECLASE IGUAL CADENA
                  | VARIABLECLASE IGUAL expresionNumerica
                  | VARIABLECLASE IGUAL hashes
                  | VARIABLECLASE IGUAL array
                  | VARIABLECLASE IGUAL input_concatenacion
                  | VARIABLE IGUAL booleanos'''
    tabla_variables[p[1]] = p[3]

def p_asignacion(p):
    """asignacion : VARIABLE IGUAL CADENA
                  | VARIABLE IGUAL expresionNumerica
                  | VARIABLE IGUAL hashes
                  | VARIABLE IGUAL SIMBOLO
                  | VARIABLE IGUAL array
                  | VARIABLE IGUAL input_concatenacion
                  | VARIABLE IGUAL booleanos
                  | VARIABLE IGUAL solicitudDatosTeclado
                  | VARIABLE IGUAL entero_a_flotante"""

    #Julio Guerrero
    tabla_variables[p[1]] = p[3]

#DEFINICION DE ARRAY
def p_elementos_array(p):
    '''elementos_array : elemento_array COMA elementos_array
                       | elemento_array '''
    
def p_elemento_array(p):
    '''elemento_array : CADENA
                      | ENTERO
                      | FLOTANTE
                      | array
                      | VARIABLE'''
    
def p_array(p):
    '''array : CORCHETE_IZ elementos_array CORCHETE_DER
             | CORCHETE_IZ CORCHETE_DER'''
    
#metodo for each arrays
def p_each_array(p):
    """each_array : VARIABLE PUNTO DO BARRA VARIABLE BARRA cuerpo_each END"""


def p_cuerpo_each(p):
    """cuerpo_each : cuerpo
                   | vacio"""

def p_vacio(p):
    "vacio : "" "

#Jose Delgado
def p_impresion_vacia(p):
    '''impresion_vacia : PRINT PARENTESIS_IZ PARENTESIS_DER
                        | PUTS PARENTESIS_IZ PARENTESIS_DER
                        | PUTS
                        | PRINTF PARENTESIS_IZ PARENTESIS_DER'''
    print("")

def p_operadoresComparacion(p):
    '''operadoresComparacion : IGUAL_DOBLEP
                             | NAVE
                             | DIFERENTE
                             | MAYOR_QUE
                             | MENOR_QUE
                             | MENOR_IGUAL_QUE
                             | MAYOR_IGUAL_QUE'''
    
def p_funcionesComparacion(p):
    '''funcionesComparacion : Y_SIGNO
                            | O_SIGNO'''


def p_expresiones_booleanas(p):
    '''expresiones_booleanas : valorSimbolo operadoresComparacion valorSimbolo 
                             | valorNumerico operadoresComparacion valorNumerico
                             | VARIABLE operadoresComparacion VARIABLE
                             | VARIABLE operadoresComparacion valorNumerico
                             | valorNumerico operadoresComparacion VARIABLE  ''' 
    
    #Cristhian Barragan y Julio Guerrero
    if p.slice[1].type == 'VARIABLE' and p.slice[3].type == 'VARIABLE':
        valor1=p[1]
        valor2=p[3]
        if valor1 not in tabla_variables and valor2 not in tabla_variables:
            error = f"Error semántico: Variable {valor1} no declarada.\nError semántico: Variable {valor2} no declarada"
            errores_semanticos.append(error)
            print(error)
            return
        elif valor1 not in tabla_variables:
            error = f"Error semántico: Variable {valor1} no declarada."
            errores_semanticos.append(error)
            print(error)
            return
        elif valor2 not in tabla_variables:
            error = f"Error semántico: Variable {valor2} no declarada"
            errores_semanticos.append(error)
            print(error)
            return
        
        #estan en la tabla me aseguro que sean valores permitidos 
        else:
            valor_var1=tabla_variables[valor1]
            valor_var2=tabla_variables[valor2]
            #dos simbolos
            if  (isinstance(valor_var1,str) and isinstance(valor_var2,str)) :
                if  (valor_var1.startswith(":") and valor_var2.startswith(":")) :
                    pass
                else: 
                    error = f"Error semántico: variables no validas para comparacion "
                    errores_semanticos.append(error)
                    print(error)
                    return
            elif (isinstance(valor_var1,int) and isinstance(valor_var2,int)) or (isinstance(valor_var1,float) and isinstance(valor_var2,float)):
                pass
            else:
                if  (isinstance(valor_var1,str) and isinstance(valor_var2,str)) :
                    if (valor_var1.startswith(":") and not valor_var2.startswith(":")) or (valor_var2.startswith(":") and not valor_var1.startswith(":")): 
                        error = f"Error semántico: ambas variables deben ser de tipo simbolo"
                        errores_semanticos.append(error)
                        print(error)
                        return

                elif (isinstance(valor_var1,int) and not isinstance(valor_var2,int)) or (isinstance(valor2,int) and not isinstance(valor1,int)): 
                    error = f"Error semántico: ambas variables deben ser de tipo int"
                    errores_semanticos.append(error)
                    print(error)
                    return
                elif (isinstance(valor_var1,str) or isinstance(valor_var2,str)) : 
                    error = f"Error semántico: uno de los elementos es string"
                    errores_semanticos.append(error)
                    print(error)
                    return
                elif (isinstance(valor_var1,float) and not isinstance(valor_var2,float)) or (isinstance(valor2,float) and not isinstance(valor1,float)): 
                    error = f"Error semántico: ambas variables deben ser de tipo float"
                    errores_semanticos.append(error)
                    print(error)
                    return

def p_solicitudDatosTeclado(p):
    '''solicitudDatosTeclado : GETS 
                            | GETS PUNTO funcionesFormatoImpresion '''

def p_funciones(p):
    '''funciones : DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER declaraciones END
                 | DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER declaraciones END
                 | DEF VARIABLE declaraciones END'''
    
def p_funcionesArray(p):
    '''funcionesArray : SORT
                      | FOR EACH'''
    
def p_funcionesFormatoImpresion(p):
    '''funcionesFormatoImpresion : CHOMP'''


def p_funcionesNumeros(p):
    '''funcionesNumeros : TO_F'''

def p_funcionesEstructuras(p):
    '''funcionesEstructuras : VARIABLE PUNTO funcionesArray
                            | VARIABLE PUNTO funcionesNumeros'''

    #Julio Guerrero
    if p[1] not in tabla_variables:
        error = f"Error semántico: Variable {p[1]} no declarada"
        errores_semanticos.append(error)
        print(error)
    else:
        for i in tabla_variables:
            if i[0] == p[1]:
                if isinstance(tabla_variables[p[1]], int):
                    pass
                else:
                    error = f"Error semántico: Variable {p[1]} no es un entero"
                    errores_semanticos.append(error)
                    print(error)
                    print(errores_semanticos)

def p_argumentos(p):
    '''argumentos : VARIABLE
                    | VARIABLE COMA argumentos'''
    
#Estructuras de Control
def p_condicionIf(p):
    '''condicionIf : expresiones_booleanas
                | EXCLAMACION_BAJO PARENTESIS_IZ expresiones_booleanas PARENTESIS_DER funcionesComparacion condicionIf
                | expresiones_booleanas funcionesComparacion condicionIf
                | EXCLAMACION_BAJO PARENTESIS_IZ expresiones_booleanas PARENTESIS_DER'''


def p_estructura_if(p):
    '''estructura_if : IF condicionIf declaraciones ELSE declaraciones END
                    | IF condicionIf declaraciones estructura_secundaria_if'''


def p_estructura_ifUnaLinea(p):
    '''estructura_ifUnaLinea : IF condicionIf declaraciones END'''



def p_estructura_secundaria_if(p):
    '''estructura_secundaria_if : ELSEIF condicionIf declaraciones ELSE declaraciones END
                                | ELSEIF condicionIf declaraciones estructura_secundaria_if'''


def p_declaracion(p):
    '''declaracion : operacionAritmetica
                    | asignacion
                    | impresion
                    | impresion_vacia
                    | expresiones_booleanas
                    | solicitudDatosTeclado
                    | hashes
                    | estructura_if
                    | asignacion_clase
                    | estructura_ifUnaLinea
                    | sentencia_while
                    | sentencia_while_bool'''

def p_declaraciones(p):
    '''declaraciones : declaracion 
                    | declaracion declaraciones'''

def p_sentencia_while_bool(p):
    '''sentencia_while_bool : WHILE declaracion declaraciones END
                            | WHILE VARIABLE declaraciones END '''
    if not isinstance(p[2], bool):
        print(f"Error: La condición del bucle while debe ser booleana, pero se encontró {type(p[2])}")
    else:
        pass

def p_sentencia_while(p):
    '''sentencia_while : WHILE expresiones_booleanas sentencia_while END
                      | WHILE expresiones_booleanas declaracion END '''

    if not isinstance(p[2], bool):
        print(f"Error: La condición del bucle while debe ser booleana, pero se encontró {type(p[2])}")
    else:
        pass

def p_sentencia_case(p):
    '''sentencia_case : CASE VARIABLE sentencia_when END'''

def p_sentencia_when(p):
    '''sentencia_when : WHEN declaracion declaracion'''

def p_sentencias_when(p):
    '''sentencias_when : sentencia_when
                    | sentencia_when sentencias_when'''


def p_sentencia_until(p):
    '''sentencia_until : UNTIL declaracion DO declaracion END'''

#estructura de datos HASH
def p_hashes(p):
    '''hashes : LLAVE_IZ elemento_hash LLAVE_DER
              | LLAVE_IZ LLAVE_DER'''

def p_claveValor(p):
    '''claveValor : VARIABLE ASIGNA_HASH valorNumerico
                  | VARIABLE ASIGNA_HASH CADENA
                  | CADENA ASIGNA_HASH valorNumerico
                  | CADENA ASIGNA_HASH CADENA'''

def p_elemento_hash(p):
    '''elemento_hash : claveValor
                     | claveValor COMA elemento_hash'''

def p_each_hash(p):
    '''each_hash : VARIABLE PUNTO EACH DO BARRA each_args_hash declaracion END'''

def p_each_args_hash(p):
    '''each_args_hash : VARIABLE COMA VARIABLE BARRA
                      | VARIABLE BARRA'''

def p_encabezadoClase(p):
    '''encabezadoClase : CLASS ID_CLASE
                    | CLASS ID_CLASE MENOR_QUE ID_CLASE'''

def p_definicion_clase(p):
    '''definicion_clase : encabezadoClase declaraciones END'''

def p_cuerpoVariables(p):
    '''cuerpoVariables : asignacion_clase                
                | asignacion
                | asignacion_clase cuerpoVariables
                | asignacion cuerpoVariables'''

def p_cuerpoClase(p):
    '''cuerpoClase : cuerpoVariables
                | declaracion
                | funciones
                '''

def p_cuerpoClaseE(p):
    '''cuerpoClaseE : cuerpoClase
                | cuerpoClase cuerpoClaseE'''
    
#Cristhian Barragan
# Error rule for syntax errors
def p_error(p):
    if p:
        errors.append(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
        parser.errok()
    else:
        errors.append(f"Syntax error at EOF")
        print(f"Syntax error at EOF")

# Construir el analizador sintáctico
parser = yacc.yacc()

def pruebas(algoritmo_file,log_prefix):
    parser = yacc.yacc()
    archivo = f"{ruta_algoritmos}/{algoritmo_file}"
    result=''
    
    with open(archivo, "r") as file:
        data = file.read()

    parser.errors = errors
    cod= parser.parse(data)
    print(cod)

    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%Y%m%d-%H%M%S") 
    nombre_archivo = f"{log_prefix}-{fecha_hora}.txt"

    ruta_archivo = f"{ruta_carpeta}/{nombre_archivo}"

    with open(ruta_archivo, "a+") as log_file:
        for error in errors:
            log_file.write("Error de sintaxis en token:", p.type, "En : " , p.value + "\n")
            print (error)

    print(f"Resultado guardado en {ruta_archivo}")

def pruebasSemantico(algoritmo_file, log_prefix):
    archivo = f"{ruta_algoritmos}/{algoritmo_file}"

    with open(archivo, "r") as file:
        for linea in file:
            if linea.strip():
                parser.parse(linea)
    file.close()
    
    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%Y%m%d-%H%M%S")
    nombre_archivo = f"{log_prefix}-{fecha_hora}.txt"

    ruta_archivo = f"{ruta_carpeta}/{nombre_archivo}"
    with open(ruta_archivo, "a+") as log_file:
        for error in errores_semanticos:
            log_file.write(error + "\n")
            print(error)

    print(f"Resultado guardado en {ruta_archivo}")

def pruebasSemanticoInterfaz(codeAnalisis):
    #tabla_variables.clear()
    parser.parse(codeAnalisis)
    nombre_archivo = "code_validation.txt"

    #vaciar txt de validacion al volver a presionar validar para q no se manden errores anteriores:)
    #agregar tokens no reconocidos a partir del analisis lexico, ejemplo si se prueba a=1@ sale Illegal character '@', eso se lo muestra en el cuadro de la validacion
    if len(errors)==0 and len(errores_semanticos)==0 and len(l.noReconocidos)==0:
        with open(nombre_archivo, "w") as log_file:
            log_file.write("Código correcto :)" + "\n")
    else:
        with open(nombre_archivo, "w") as log_file:
            for error in l.noReconocidos:
                log_file.write(error + "\n")
                print(error)
        with open(nombre_archivo, "a+") as log_file:
            for error in errores_semanticos:
                log_file.write(error + "\n")
                print(error)
        with open(nombre_archivo, "a+") as log_file:
            for error in errors:
                log_file.write(f"{error} \n")
                print (error)
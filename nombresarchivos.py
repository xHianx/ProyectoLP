import datetime


# CREACION DE ARCHIVO
FECHA = datetime.datetime.now().date()
HORA = datetime.datetime.now().hour
MINUTO = datetime.datetime.now().minute

# Josemiu | xHianx | julioguerrero131 
USUARIO = "xHianx"

# Se imprimen logs del lexico y sintactico en cada prueba
# "algoritmo2_Julio_Guerrero.rb"
# "algoritmo3_Cristhian_Barragan.rb"
# "algoritmo1_Jose_Miguel_Delgado.rb"
file_path_read = "algoritmo3_Cristhian_Barragan.rb"
file_path_write_lex = f"logs/lexico-{USUARIO}-{FECHA}-{HORA}-{MINUTO}.txt".replace(":", "-")
file_path_write_sint = f"logs/sintactico-{USUARIO}-{FECHA}-{HORA}-{MINUTO}.txt".replace(":", "-")
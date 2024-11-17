import datetime


# CREACION DE ARCHIVO
FECHA = datetime.datetime.now().date()
HORA = datetime.datetime.now().hour
MINUTO = datetime.datetime.now().minute

# Josemiu | xHianx | julioguerrero131 
USUARIO = "xHianx"

# sintactico | lexico
TIPO_ANALISIS = "sintactico"

file_path_read = "algoritmodeprueba_Jose_Miguel_Delgado.rb"
file_path_write = f"logs/{TIPO_ANALISIS}-{USUARIO}-{FECHA}-{HORA}-{MINUTO}.txt".replace(":", "-")
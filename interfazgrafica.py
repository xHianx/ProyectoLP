import tkinter as tk
from PIL import Image, ImageTk
import proyectolpsintactico as s
import lplexico as l
from lplexico import tokens, lexer


def validar():
    #tomar lo del la textbox
    #guarda en code_output
    save_to_file()
    # #parser guarda en validation y lo carga en la pantalla 
    load_from_file()
        
    pass

def load_from_file():
    s.tabla_variables.clear()
    s.errores_semanticos.clear()
    l.noReconocidos.clear()
    s.errors.clear()
    stringAnalisis=""
    codigo=open("code_output.txt","r")
    for linea in codigo.readlines():
        stringAnalisis = stringAnalisis + " "+ linea.strip()
          
    with open("code_output.txt", "w") as file:
        file.write(stringAnalisis)
    
    file=open("code_output.txt","r")
    for linea in file.readlines():
        lexer.input(linea)
        s.pruebasSemanticoInterfaz(linea)

    try:
        with open("code_validation.txt", "r") as file:
            file_content = file.read()
        texto_codigo1.delete("1.0", tk.END)
        texto_codigo1.insert(tk.END, file_content)

        
    except FileNotFoundError:
        texto_codigo1.delete("1.0", tk.END)
        texto_codigo1.insert(tk.END, "No se encontró el archivo 'code_validation.txt'.")

def save_to_file():
    code_content = texto_codigo.get("1.0", tk.END)
    with open("code_output.txt", "w") as file:
        file.write(code_content)

def limpiar():
    # Limpiar el área de texto de código
    texto_codigo.delete('1.0', tk.END)
    
    # Limpiar el área de texto de resultados
    texto_codigo1.delete('1.0', tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("RubyAnalyzer")
root.configure(bg="#00303F")
root.geometry("1200x700")

# Crear la barra de navegación
barra_navegacion = tk.Frame(root, bg="#004D40", height=60)
barra_navegacion.pack(side=tk.TOP, fill=tk.X)

# Frame para centrar el contenido de la barra de navegación
frame_centrado_nav = tk.Frame(barra_navegacion, bg="#004D40")
frame_centrado_nav.pack(expand=True, fill=tk.X)

# Logo
imagen = Image.open("logo.png")
imagen = imagen.resize((60, 60), Image.Resampling.LANCZOS)
foto = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(frame_centrado_nav, image=foto, bg="#004D40")
label_imagen.pack(side=tk.LEFT, padx=10, expand=True, anchor=tk.E)

# Etiqueta en la barra de navegación
etiqueta_barra = tk.Label(frame_centrado_nav, text="Analizador Ruby", fg="white", font=("Arial", 20, "bold"), bg="#004D40")
etiqueta_barra.pack(side=tk.LEFT, padx=10, expand=True, anchor=tk.W)

# Resto del código permanece igual (desde la sección de instrucciones hasta el final)
# Recuadro de instrucciones
recuadro_instrucciones = tk.Frame(root, bg="#00303F", padx=20, pady=20)
recuadro_instrucciones.pack(side=tk.TOP, fill=tk.X)

titulo_instrucciones = tk.LabelFrame(recuadro_instrucciones, text="Instrucciones", bg="#1F4D4D", fg="white", padx=10, pady=10)
titulo_instrucciones.pack(fill=tk.BOTH, expand=True)

etiqueta_instrucciones = tk.Label(titulo_instrucciones, text="Para validar, escribe el código dentro del recuadro Código y haz clic en 'Validar'.", bg="#00303F", fg="white", font=("Arial", 14))
etiqueta_instrucciones.pack(fill=tk.BOTH, expand=True)

# Crear una sección de contenido
contenedor_principal = tk.Frame(root, bg="#00303F")
contenedor_principal.pack(fill=tk.BOTH, expand=True)

# Crear un frame para el código y el resultado
frame_principal = tk.Frame(contenedor_principal, bg="#00303F", padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Crear los recuadros lado a lado
frame_recuadros = tk.Frame(frame_principal, bg="#00303F")
frame_recuadros.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Recuadro para el código de entrada
recuadro_codigo = tk.Frame(frame_recuadros, bg="#004D40", padx=10, pady=10)
recuadro_codigo.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

titulo_codigo = tk.LabelFrame(recuadro_codigo, text="Código", bg="#1F4D4D", fg="white", padx=10, pady=10)
titulo_codigo.pack(fill=tk.BOTH, expand=True)
frame_texto_codigo = tk.Frame(titulo_codigo)
frame_texto_codigo.pack(fill=tk.BOTH, expand=True)
texto_codigo = tk.Text(frame_texto_codigo, width=60, height=15, bg="#263238", fg="white", insertbackground="white")
texto_codigo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de desplazamiento para el código
scrollbar_codigo = tk.Scrollbar(frame_texto_codigo, orient=tk.VERTICAL, command=texto_codigo.yview)
scrollbar_codigo.pack(side=tk.RIGHT, fill=tk.Y)
texto_codigo.config(yscrollcommand=scrollbar_codigo.set)

# Recuadro para los resultados
recuadro_resultados = tk.Frame(frame_recuadros, bg="#004D40", padx=10, pady=10)
recuadro_resultados.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

titulo_resultados = tk.LabelFrame(recuadro_resultados, text="Resultado", bg="#1F4D4D", fg="white", padx=10, pady=10)
titulo_resultados.pack(fill=tk.BOTH, expand=True)
frame_texto_resultados = tk.Frame(titulo_resultados)
frame_texto_resultados.pack(fill=tk.BOTH, expand=True)
texto_codigo1 = tk.Text(frame_texto_resultados, width=60, height=15, bg="#263238", fg="white", insertbackground="white")
texto_codigo1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de desplazamiento para los resultados
scrollbar_resultados = tk.Scrollbar(frame_texto_resultados, orient=tk.VERTICAL, command=texto_codigo1.yview)
scrollbar_resultados.pack(side=tk.RIGHT, fill=tk.Y)
texto_codigo1.config(yscrollcommand=scrollbar_resultados.set)

# Crear los botones en la parte inferior (centrados)
barra_botones = tk.Frame(root, bg="#004D40", padx=10, pady=10)
barra_botones.pack(side=tk.BOTTOM, fill=tk.X)

# Frame interno para centrar los botones
frame_centrado = tk.Frame(barra_botones, bg="#004D40")
frame_centrado.pack(expand=True)

boton_validar = tk.Button(frame_centrado, text="Validar", command=validar, bg="#FF5722", fg="white", width=15, height=2, font=("Arial", 12, "bold"))
boton_validar.pack(side=tk.LEFT, padx=10)

boton_limpiar = tk.Button(frame_centrado, text="Limpiar", command=limpiar, bg="#FF5722", fg="white", width=15, height=2, font=("Arial", 12, "bold"))
boton_limpiar.pack(side=tk.LEFT, padx=10)

# Mantener una referencia a la imagen del logo
root.imagen = foto

# Ejecutar el bucle principal de la aplicación
root.mainloop()
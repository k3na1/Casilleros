import os
import time

def escribirArchivo(contenido, rutaArchivo):                                 #Función para escribir en el contenido.txt
    try:
        with open(rutaArchivo, 'a', encoding='utf-8') as txt:
            txt.write(contenido + "\n")
            resultado = "\nDatos agregados"
    except Exception as e:
        resultado = f"\nError en el programa, solicite ayuda al operador\n{e} "
    return resultado

def buscarUsuario(nombre, rutaArchivo):                                      #Función para buscar un usuario en el contenido.txt
    try:
        with open(rutaArchivo, 'r') as txt:
            lineas = txt.readlines()
            nombre = nombre.upper()
            noEncontrado = True
            for linea in lineas:
                if nombre in linea.upper():
                    print(f"Usuario encontrado: {linea.strip()}")
                    noEncontrado = False
            if noEncontrado:
                print("Usuario no encontrado")
    except Exception as e:
        print(f"\nError en el programa, solicite ayuda al operador\n{e}")

def borrarUsuario(nombre, rutaArchivo):
    try:
        with open(rutaArchivo, 'r+', encoding='utf-8') as txt:
            lineas = txt.readlines()
            txt.seek(0)
            borrado = False
            for linea in lineas:
                if nombre not in linea:
                    txt.write(linea)
                else:
                    borrado = True
            txt.truncate()
            if borrado:
                print("Usuario borrado")
            else:
                print("Usuario no encontrado")
    except Exception as e:
        resultado = f"\nError en el programa, solicite ayuda al operador\n{e} "
        return resultado
    
def contadorUsuarios(nombre, rutaArchivo):
    try:
        with open(rutaArchivo, 'r') as txt:
            lineas = txt.readlines()
            nombre = nombre.upper()
            noEncontrado = True
            contador = 0
            for linea in lineas:
                if nombre in linea.upper():
                    contador += 1
            return contador
    except Exception as e:
        print(f"\nError en el programa, solicite ayuda al operador\n{e}")



while True:
    rutaArchivo = os.path.abspath(__file__)                                 #Verificador de archivos dentro del directorio
    directorioArchivo = os.path.dirname(rutaArchivo)
    nombreArchivo = 'contenido.txt'
    rutaArchivo = os.path.join(directorioArchivo, nombreArchivo)           # Construye la ruta completa al archivo

    if not os.path.isfile(rutaArchivo):
        with open(f'{directorioArchivo}/contenido.txt', 'w', encoding='utf-8') as archivo:    #Si no existe me crea el contenido.txt y continúa
            archivo.write("")
        print("Archivo no encontrado, generando...")
        time.sleep(3)
        print("Archivo generado con éxito\nContinuando...")
        time.sleep(3)
        os.system("cls")
    else:
        while True:
            print("""
                    ===== MENÚ =====

                1)Escribir nuevo usuario
                2)Buscar usuario
                3)Eliminar usuario
                """)
            opc = int(input("Opción: "))
            if opc == 1:
                nombreNuevo = input("Nombre completo: ")
                rutUser = input("Rut: ")
                casillero = input("Casillero: ")
                resultado = nombreNuevo + " " + "\t\t\t" + "Rut: " + rutUser + "\t\t" + "Casillero: " + casillero
                print (escribirArchivo(resultado, rutaArchivo))
            elif opc == 2:
                nombreUser = input("Escriba el nombre, Rut o casillero del alumno a buscar: ")
                buscarUsuario(nombreUser, rutaArchivo)
            elif opc == 3:
                nombreUser = input("Escriba el nombre, Rut o casillero del alumno a borrar: ")
                contador = contadorUsuarios(nombreUser, rutaArchivo)
                if contador >= 1:
                    print(f"Se han encontrado {contador} resultado/s")
                    print("\n¿Está seguro de borrar los resultados?\n1) Si\n2) No")
                    opc2 = int(input("Opción: "))
                    if opc2 == 1:
                        borrarUsuario(nombreUser, rutaArchivo)
                else:
                    print("No se han encontrado resultados")
                    
                



import json
'''
1. El programa debe tener un menú que permita al usuario seleccionar diferentes opciones:
agregar cita, buscar cita, modificar cita, cancelar cita y salir del programa.
2. Cada cita médica debe tener los siguientes datos: nombre del paciente, fecha de la cita,
hora de la cita y motivo de la consulta.
3. Al agregar una cita, el programa debe solicitar al usuario que ingrese los datos
correspondientes y luego guardar la cita en un archivo JSON.
4. Al buscar una cita, el programa debe solicitar al usuario un criterio de búsqueda (por
ejemplo, nombre del paciente o fecha de la cita) y mostrar todas las citas que coincidan
con ese criterio.
5. Al modificar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y solicitar los nuevos datos para actualizarla en el archivo JSON.
6. Al cancelar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y eliminarla del archivo JSON.
7. Al salir del programa, se deben guardar todos los cambios realizados en el archivo JSON
y mostrar un mensaje de despedida.

'''
import json

def agregar_cita():
    nombre = input("Ingrese el nombre del paciente: ")
    fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    motivo = input("Ingrese el motivo de la consulta: ")
    
    cita = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo
    }
    
    with open("citas.json", "a") as archivo:
        json.dump(cita, archivo, indent=4)
        archivo.write("\n")
    
    print("Cita agregada correctamente.")

def buscar_cita():
    criterio = input("Ingrese el criterio de búsqueda (nombre o fecha): ")
    valor = input("Ingrese el valor a buscar: ")
    
    with open("citas.json", "r") as archivo:
        citas = archivo.readlines()
    
    citas_encontradas = []
    
    for cita in citas:
        cita_json = json.loads(cita)
        if cita_json[criterio] == valor:
            citas_encontradas.append(cita_json)
    
    if citas_encontradas:
        print("Citas encontradas:")
        for cita in citas_encontradas:
            print("Nombre: ", cita["nombre"])
            print("Fecha: ", cita["fecha"])
            print("Hora: ", cita["hora"])
            print("Motivo: ", cita["motivo"])
            print("------------------------")
    else:
        print("No se encontraron citas con ese criterio.")

def modificar_cita():
    with open("citas.json", "r") as archivo:
        citas = archivo.readlines()
    
    if not citas:
        print("No hay citas para modificar.")
        return
    
    print("Seleccione la cita que desea modificar:")
    for i, cita in enumerate(citas):
        cita_json = json.loads(cita)
        print(f"{i+1}. Nombre: {cita_json['nombre']} - Fecha: {cita_json['fecha']} - Hora: {cita_json['hora']}")
    
    opcion = int(input("Ingrese el número de la cita a modificar: ")) - 1
    
    if opcion < 0 or opcion >= len(citas):
        print("Opción inválida.")
        return
    
    cita_json = json.loads(citas[opcion])
    
    nombre = input("Ingrese el nuevo nombre del paciente: ")
    fecha = input("Ingrese la nueva fecha de la cita (DD/MM/AAAA): ")
    hora = input("Ingrese la nueva hora de la cita (HH:MM): ")
    motivo = input("Ingrese el nuevo motivo de la consulta: ")
    
    cita_json["nombre"] = nombre
    cita_json["fecha"] = fecha
    cita_json["hora"] = hora
    cita_json["motivo"] = motivo
    
    citas[opcion] = json.dumps(cita_json, ensure_ascii=False, indent=4)
    
    with open("citas.json", "w") as archivo:
        archivo.write("\n".join(citas))
    
    print("Cita modificada correctamente.")

def cancelar_cita():
    with open("citas.json", "r") as archivo:
        citas = archivo.readlines()
    
    if not citas:
        print("No hay citas para cancelar.")
        return
    
    print("Seleccione la cita que desea cancelar:")
    for i, cita in enumerate(citas):
        cita_json = json.loads(cita)
        print(f"{i+1}. Nombre: {cita_json['nombre']} - Fecha: {cita_json['fecha']} - Hora: {cita_json['hora']}")
    
    opcion = int(input("Ingrese el número de la cita a cancelar: ")) - 1
    
    if opcion < 0 or opcion >= len(citas):
        print("Opción inválida.")
        return
    
    del citas[opcion]
    
    with open("citas.json", "w") as archivo:
        archivo.write("\n".join(citas))
    
    print("Cita cancelada correctamente.")

def salir():
    print("¡Hasta luego!")

def mostrar_menu():
    print("Bienvenido al programa de citas médicas")
    print("Seleccione una opción:")
    print("1. Agregar cita")
    print("2. Buscar cita")
    print("3. Modificar cita")
    print("4. Cancelar cita")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            agregar_cita()
        elif opcion == "2":
            buscar_cita()
        elif opcion == "3":
            modificar_cita()
        elif opcion == "4":
            cancelar_cita()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()




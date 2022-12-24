import db
import os

def cls():
    os.system("cls")

bigText = """
   |             '            |/| 
/~~|/~~||/~\ /~\ |/~~||/~\   ~|~| 
\__|\__||   |   ||\__||   |__ |_|_
"""

while True:
    cls()
    print(bigText)
    print("-------------------------------")
    print("1) Iniciar sesión   ")
    print("2) Crear usuario    ")
    print("3) Eliminar usuario ")
    print("4) Editar usuarios  ")
    print("5) Mostrar usuarios ")
    op = int(input("Introduce la opción: "))

    if op == 1:
        db.iniciarSesion()
    elif op == 2:
        cus = db.crearUsuario()
        gus = db.guardarUsuario(cus)
        print(gus['contenido'])
        input("Presiona cualquier tecla para continuar... ")
    elif op == 3:
        user = str(input("Introduce el nombre de usuario a eliminar: "))
        db.eliminarUsuario(user)
    elif op == 4:
        user = str(input("Introduce el nombre de usuario a editar: "))
        db.editarUsuario(user)
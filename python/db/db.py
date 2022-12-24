import os
import pymysql

def conectarDB(sentencia, valores, tipoC):
    mensaje = {
        "contenido":"",
        "datos":[]
    }

    try:
        conectar = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            db = 'damian_t1'
        )

        cursor = conectar.cursor()
        if tipoC == 1:
            cursor.execute(sentencia, (valores))
        else:
            cursor.execute(sentencia)
        mensaje['datos'] = cursor.fetchall()
        conectar.commit()
        conectar.close()

        mensaje['contenido'] = "✅"
    except:
        mensaje['contenido'] = "❌"
    return mensaje

def passCheck(user, password):
    sentencia = "SELECT password FROM usuarios WHERE user = %s"
    resp = conectarDB(sentencia, user, 1)
    _resp = resp['datos']
    
    if password == _resp[0][0]:
        return True
    else:
        return False

def iniciarSesion():
    usuario = str(input("Usuario: "))
    contraseña = str(input("Contraseña: "))
    c = passCheck(usuario, contraseña)
    if c == True:
        print("Si es")
    else:
        print("No es")
    input("")

def checkRole():
    print("--- Debes iniciar sesión ---")
    usuario = str(input("Usuario: "))
    contraseña = str(input("Contraseña: "))
    valPass = passCheck(usuario, contraseña)
    if valPass == True:
        sentencia = "SELECT role FROM usuarios WHERE user = %s"
        rol = conectarDB(sentencia, usuario, 1)
        _rol = rol['datos']

        if int(_rol[0][0]) >= 3:
            return True
        elif int(_rol[0][0]) < 3:
            return False

    else:
        print("Contraseña Incorrecta")

def crearUsuario():
    valRol = checkRole()
    if(valRol == True):
        user = str(input("Introduce el nombre de usuario: "))
        password = str(input("Introduce la contraseña de usuario: "))
        role = int(input("Introduce el rol del usuario: "))

        data = {
            "user":user,
            "password":password,
            "role":role
        }

        return data
    else:
        print("No tienes permisos suficientes...")

def guardarUsuario(datos):
    sentencia = "INSERT INTO usuarios (user, password, role) VALUES (%s, %s, %s)"
    valores = datos['user'], datos['password'], datos['role']
    return conectarDB(sentencia, valores, 1)


def eliminarUsuario(user):
    valRol = checkRole()
    if(valRol == True):
        sentencia = "DELETE FROM usuarios WHERE user = %s"
        return conectarDB(sentencia, user, 1)
    else:
        print("No tienes permisos suficientes")

def editarUsuario(user):
    dus = crearUsuario()
    sentencia = "UPDATE usuarios SET user = %s, password = %s, role = %s"
    return conectarDB(sentencia, dus, 1)
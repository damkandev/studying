# [Severity 1] Injection
Las vulnerabilidades de inyección son muy comunes hoy en dia, se producen por que en una entrada controlada el valor se interpreta como comando o parametros reales, todo esto siempre dependera de las tecnologias que se usen, acá hay algunos ejemplos.

1. **SQL Injection:** Esto sucede cuando se pasan *entradas* que el usuario introduce para manipular el resultado de la query.
2. **Command Injection:** Esto ocurre cuando la entrada del usuario se pasa a los comandos del sistema, lo que por resultado da que se interactue de forma directa con la consola de comandos y todo lo que ello conlleva.

Si un atacante es capaz de modificar la consulta con exito, seria capaz de hacer los siguientes ejemplos:

1. **Acceder**, **Modificar** y **Borrar** información en una base de datos, es decir que puede robar información sensible, ejecutar comandos y llevar más ataques vinculados al sitio.
2. **Ejecutar** comandos arbitrarios en el sistema pudiendo obtener acceso a los sistemas de los usuarios, nuevamente podría robar datos e información sensible.

Una de las principales defensas es asegurarse que las entradas en las que interactua el usuario no se comporten como comandos o parametros, hay varias formas de hacerlo:

1. Utilizar una lista de *entradas* permitidas con una lista de palabras o caracteres seguros, en caso contrario se rechaza y la aplicación lanza un error.
2. Eliminación de la *entrada*, antes de que los caracteres o palabras maliciosos sean procesados se eliminen.

Los “Dangerous Characters Or Input” es clasificado como cualquier entrada que pueda modificar la forma en la que se procesan los datos.

# [Severity 1] OS Command Injection
La inyección de comandos se produce cuando ==El código del lado del servidor== en una aplicación web realiza una llamada a la *“Hosting Machine”* permitiendo al atacante ejecutar comandos, desde algo no tan malicioso como un `whoami` o la lectura de archivos hasta una *reverse shell* que se puede realizar tan solo con `;nc -e /bin/bash`.

Una vez el atacante tiene un punto de apoyo puede empezar a ==Pivotear== alrededor.

# [Severity 1] Command Injection Practical

#### Inyección Ciega
La inyección ciega se da cuando el servidor no muestra la respuesta en el archivo HTML.

#### Inyección Activa
La inyección activa de comandos devolvera la respuesta al usuario, puede hacerse visible a través de varios elementos HTML.

### Ejemplo de Practica:
EvilCorp ha empezado a desarrollar una shell basado en web, pero accidentalmente lo ha dejado expuesto a internet, pero esta vez la respuesta podra ser vista en la página. (==Inyección Activa==).

Pero antes veamos el codigo de evilshell.php y repasemos que esta haciendo.

![[Pasted image 20230109012311.png]]

### Formas de detectar Inyección Activa
A continuación veremos algunos comandos que podemos usar para detectar una Inyección Activa.

**Linux:**
1. whoami
2. id
3. ifconfig/ip addr
4. uname -a 
5. ps -ef

**Windows:**
1. whoami
2. ver
3. ipconfig
4. tasklist
5. netstat -an

# [Severity 2] Broken Authentication 
![[Pasted image 20230109112337.png]]
El usuario introduce sus credenciales y el servidor las verifica, si son correctas el servidor proporcionara al navegador una **Cookie 🍪**, una *Cookie de Sesión* es necesaria ya que los servidores webs utilizan HTTP(S) para comunicarse, conectar las *cookies de sesión* hara que el servidor sabra quien envia datos, asi el servidor puede hacer un seguimiento de las acciones de los usuarios.

Si un atacante encuentra fallos en un sistema de autenticación, podria acceder datos sensibles, algunos fallos comunes en estos mecanismos son:

- **Brute Force Attacks:** si una aplicación web usa *username* y *password* un atacante es capaz de lanzar un ataque de ==Fuerza Bruta== le permitira adivinar el *username* y la *password*.
- **Use of weak credentials:** Si una aplicación web no tiene politicas de contraseñas seguras y permite contraseñas como “password1” y otras contraseñas comunes, entonces el atacante sera capaz de adivinar la contraseña y usuario.
- **Weak Session Cookies 🍪:** Las cookies de sesión son el como el servidor mantiene un seguimiento de los usuarios, si las cookies contienen valores predicables, un atacante puede asignarse sus propias cookies y acceder a las cuentas de otros usuarios.

# [Severity 2] Broken Authentication Practical
Muchas veces sucede que los desarrolladores se olvidan de sanitizar la entrada (*username* y *password*) dada por el usuario en su código, lo que los hace vulnerables por ejemplo a SQLi, ahora nos centraremos en una vulnerabilidad que ocurre por un fallo del desarrollador, pero es muy facil de explotar.

Vamos a entender con ayuda de un ejemplo, acá tenemos un usuario existente el cual es **admin**, pero lo que haremos sera intentar re-registrarnos con ese mismo nombre de usuario pero con una ligera modificación, nosotros introduciremos “ admin” (notar el espacio), ahora cuando tu ingresas este *username* y introduces otra información requerida como *email* o *password* y te subes la información, actualmente te registraste en un nuevo usuario pero este usuario tendra los mismos privilegios que un administrador normal.


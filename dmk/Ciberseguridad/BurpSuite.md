# BurpSuite - Dashboard
Cuando accedemos a BurpSuite quizá no entenderemos nada de lo que aparece pero en resumen se divide en 4 partes.
 ![[Pasted image 20230108124459.png]]
 Esto es dado que se divide en 4 partes, las cuales son las siguientes:
 - **1) El Menu de tareas (Tasks Menu):** nos permite definir tareas que se harán en segundo mientras que BurpSuite se ejecuta.
 - **2) Registro de Eventos (Event Log):** Nos mostrará todos los eventos que estén sucediendo en BurpSuite, por ejemplo “starting the Proxy…”.
 - **3) Issue Activity:** Sirve para listar todas las vulnerabilidades encontradas, pero no nos servira de nada en la versión de BurpSuite Community.
 - **4) Sección de Avisos (Advisory Section):** nos dará más información de las vulnerabilidades.
![[Pasted image 20230108131505.png]]
Puedes hacer un escaneo a un sitio web dando click en “New Scan”.
# BurpSuite - Navigation
Normalmente la navegación en la interfaz de BurpSuite se realiza a traves de las barras de menús superiores.
![[Pasted image 20230108132148.png]]
Como podemos ver, si uno de estos apartados tiene más subcategorías las podremos seleccionar en el menú que se despliegue.
En adición hacia la barra de navegación, BurpSuite también tiene atajos de teclados que permiten una navegación más rápida.

| Atajo            | Funcion                     |
| ---------------- | --------------------------- |
| Ctrl + Shift + D | Cambia al Dashboard         |
| Ctrl + Shift + T | Cambia al tablero de Target |
| Ctrl + Shift + P | Cambia a Proxy Tab          |
| Ctrl + Shift + I | Cambia a Intruder Tab       |
| Ctrl + Shift + R | Cambia a Repeater Tab


# BurpSuite - Proxy
Esta es una de las herramientas más importantes y fundamentales, nos permite capturar y manipular respuestas HTTP.
![[Untitled-2023-01-08-1402(1).png]]
Por ejemplo, si realizamos un proxy en un sitio web y el cliente envió una petición, no podrá avanzar a los servidores del sitio a menos que expresamente se lo permitamos.
Cuando abrimos la sección del proxy tenemos mucha información importante, pero lo más interesante sucede cuando interceptamos una request.
![[Pasted image 20230108141722.png]]

Cuando esto ocurre, el navegador que hace la petición se detendrá y aparecerá en nuestra pestaña de proxy dándonos las posibilidades de enviar (drop) o eliminar (forward). También podemos hacer otras cosas como enviar la petición a otros paneles e incluso exportarla como comando cURL o guardarla en un archivo.

Cuando hayamos terminado podemos hacer click en el botón de “intercept is on” para desactivar la intercepción, lo que permitirá que las peticiones pasen a través del proxy sin ser detenidas.

**Importante:** BurpSuite seguirá por defecto registrando las peticiones realizadas aun si el modo de interceptar está inactivo, pudiendo así volver atrás aun cuando no las hayamos capturado.

Los registros se pueden ver yendo al apartado de “HTTP history” y “WebSocket History“.

![[Pasted image 20230108161606.png]]

También hay opciones específicas de proxy que podemos ver en “Options”.

**Ejemplo:** el proxy no interceptará las respuestas del servidor, a menos que se lo pidamos explícitamente, podemos anular la configuración por defecto seleccionando la casilla “Intercept responses based on the following rules” eligiendo una o más reglas. La regla “Or Request Was Intercepted” es buena para capturar todas las respuestas que fueron interceptadas por el proxy.

![[Pasted image 20230108162556.png]]

Otra sección bastante útil “Match and Replace”, te permite aplicar expresiones REGEX puedes automáticamente cambiar tú *user agent* para emular un navegador diferente o eliminar todas las cookies, de nuevo eres libre de crear tus propias reglas.

# BurpSuite - Connection Through The Proxy (FoxyProxy)

Vamos a configurar nuestro navegador web local para proxy, nuestro tráfico a través de BurpSuite, esto es más común y, por lo tanto, o será el foco de esta tarea.

El BurpProxy funciona abriendo una _”Web Interface” en _127.0.0.1:8080_ (por defecto) como implica el hecho de que se trata de un proxy necesitamos redirigir todo el tráfico de nuestro navegador a través de este puerto antes de que podamos empezar a interceptarlo con Burp. Podemos hacer esto alterando la configuración del navegador o en nuestro caso usando la extension Foxy Proxy.

Esta nos permite guardar perfiles con de proxy, lo que significa que podemos cambiar rapido a nuestro perfil Burp Suite.

# BurpSuite - Scoping and Targeting
Si queremos que BurpSuite deje de capturar todas las peticiones que suceden en nuestro navegador y queremos solo centrarnos en un objetivo, podemos hacerlo desde la categoria *Target* en la sección de *Scope* y seleccionaremos el objetivo.

Aunque es una categoria bastante util tenemos otras tres más que son bastantes importantes.
1. **Site Map:** nos permite mapear las aplicaciones a las que nos dirigimos en una estructura de arbol y asi generar automaticamente un mapa simplemente navegando por el sitio, esto puede ser muy util si queremos mapear una API, cada que visitemos una página, cualquier *endpoint*.
2. **Scope:** Nos permite controlar el alcance del proyecto.
3. **Issue Definitions:** Nos proporciona una enorme lista de vulnerabilidades web completa y con descripciónes que podemos utilizar si necesitamos citas para un informe.


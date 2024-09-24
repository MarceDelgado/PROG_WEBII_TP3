# PROG_WEBII_TP3
![Documento A4 Portada Proyecto Acuarela Azul](https://github.com/user-attachments/assets/b4306bbd-f249-485f-9160-24b246761770)


Objetivo: El objetivo de este trabajo práctico es que las/os estudiantes desarrollen un proyecto
llamado Blog y una aplicación denominada post utilizando Django y el patrón de diseño
MVT. Se espera que implementen funcionalidades esenciales para la gestión de
publicaciones (post) en un blog, trabajando con vistas, plantillas y modelos, así como la
integración con GitHub y el uso de un entorno virtual. En forma adicional se busca que los
estudiantes puedan implementar un middleware personalizado y que habiliten y utilicen el
middleware de autenticación que provee Django.
Una vez dentro de nuestro entorno, y con Django instalado y el repositorio ya realizados, realizare la creación de nuestro proyecto “Blog”, con el comando django-admin startproyect Blog.
Ingreso a Blog y dentro de este realizo la creación de la aplicación “post”, mediante el comando python3 manage.py startapp post.
Al terminar de realizar todos estos pasos, realizare la clonación del proyecto al GibHub, mediante el comando git clone https://github.com/MarceDelgado/PROG_WEBII_TP3.git.
Esto nos permite:
Guardar versiones del código para ver cambios o volver a versiones anteriores.
Colaborar fácilmente con otros desarrolladores.
Hacer una copia de seguridad en la nube.
Automatizar despliegue y pruebas con herramientas CI/CD.
Mostrar mi trabajo en un portafolio público.
Es una forma eficiente de trabajar en equipo, proteger mi proyecto y mantener todo organizado.
Ahora sí estamos listos para comenzar con nuestro nuevo proyecto.
Tareas a Realizar
Las/os estudiantes deben desarrollar una aplicación llamada post, que permita la gestión
de publicaciones. A continuación, se detallan las funcionalidades específicas que debe
implementar la aplicación:
Primeramente, debemos realizar la configuración de nuestro app, haciendo las modificaciones que necesiten en el archivo setting.py, este se encuentra dentro de la carpeta “Blog”.
Para poder empezar a trabajar en nuestra aplicación “post”, configuraremos los archivos que componen la aplicación “post".
Comenzare por el  archivo models.py debe realizarse primeramente antes que las vistas y las plantillas html, ya que en él definimos los datos, después implementamos las vistas en views.py porque estás usan los modelos para recuperar o modificar datos, y pasar esa información a las plantillas HTML. Las vistas dependen de los modelos, por lo que el archivo models.py debe estar definido antes de que las vistas puedan utilizarlos, y por último las Plantillas HTML, estas se usan para mostrar la información que las vistas les pasan. Por lo tanto, las plantillas se crean después de que los modelos y las vistas están definidos, ya que necesitan tanto los datos como la lógica de las vistas para que mi aplicación funcione correctamente. 
Desarrollo de la aplicación.

1. Crear una nueva publicación (Crear)
Los usuarios podrán crear nuevas publicaciones (posts) de blog desde una interfaz web.
Formulario: El formulario de creación debe permitir ingresar al menos:
   Título de la publicación.
   Contenido (texto).
   Fecha de publicación (puede ser automática o seleccionada).
   Autor (debe estar precargado con el usuario autenticado).
Vista: Crear una vista basada en clase o función que permita el procesamiento de este formulario y la creación de una nueva publicación.
Plantilla: Crear una plantilla HTML que muestre el formulario para ingresar los datos de la nueva publicación.

Mi vista está basada en clase, porque simplifican las tareas comunes, facilitan la reutilización de código, y mantienen el código más organizado.
Por lo que me pareció más práctico para este proyecto.
La plantilla la denomine “post_crear.html”, está extiende a la plantilla base.html la cual depende de la carpeta templates.
Esta tiene un formulario donde se coloca el título, y el contenido de la publicación, debajo del contenido tiene el botón tipo “submit”, de “Crear Publicación”, se usa para enviar el formulario que crea una nueva publicación en tu aplicación web. Cuando el usuario hace clic en "Crear Publicación", los datos del formulario se envían al servidor para procesarlos y guardarlos.
Debajo de este, se encuentra el enlace “Cancelar”, donde el usuario es redirigido a la vista correspondiente a 'post_lista', cancelando cualquier acción actual sin enviar ningún formulario o guardar cambios.










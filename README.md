#BLOG CON DJANGO

Este es un proyecto web desarrollado con Django para publicar articulos de cualquier tipo. Permite indicar el nombre del autor, la categoria, el cuerpo del articulo y su fecha de publicación. Además posee un navegador que nos permite filtrar posts por autor o categoria.

##Tecnologías aplicadas:
-Python
-Django
-HTML & CSS
-Bootsrap

¿Como probarlo?

1. Clonar el repositorio:
git clone 

2. Crear y activar el entorno virtual:
python -m venv env 
env\Scripts\activate

3. Instalar dependencias
pip install django

4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

5. Crear superuser (opcional)
python manage.py createsuperuser

6. Ejecutar el servidor
python manage.py runserver

7. Acceder a: 
http://127.0.0.1:8000/

Dentro de la web:

En inicio podemos ver un poco de informacion. En la barra de navegacion que se ubica en la parte superior podemos ver lo siguiente: Inicio, Autores, Categorias y Posts.

En Autores podemos insertar el nombre de un autor junto con su gmail. Es importante hacer este paso antes de crear un post. Luego ya no hará falta introducir sus datos nuevamente.

En categoría nos pide el nombre de la categoria del post (deportivo, cientifico, policial, etc) junto con una breve descripcion. Este paso también es importante hacerlo antes de publicar un post.

En post, podemos insertar una publicacion completando cada uno de los campos que nos pide. El autor y la categoria se completan seleccionando el nombre de estos mismos, ya que estaran almacenados en la base de datos.

Volviendo al inicio, veremos un buscador. Este buscador nos permite filtrar posts por autor y categoria. Cuando apretamos el boton "filtrar", nos lleva a la seccion de posts. Alli veremos listados cada uno de los posts (si es que hay) con su respectiva informacion. Acá podemos filtrar y ver los posts unicamente de un autor en especifico o categoria si es que asi lo queremos.
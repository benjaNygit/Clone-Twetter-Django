# Clone-Twetter-Django
Clone de la red social Twetter hecho con el framework Django. Este proyecto es de practica.

## Instrucciones de uso
Para poder usar el proyecto sigue los siguientes pasos:

1. Clonar este repositorio.
2. Crear el ambiente de desarrollo local venv e instalar las dependencias.
3. Crear el archivo _.env_ en la raíz del proyecto.
4. Poner la siguiente estructura dentro del _.env_
```
SECRET_KEY_DJANGO = ''
```
5. Generar el secret key de django. Desde la shell de django.
```
from django.core.management.util import get_random_secret_key
get_random_secret_key()
```
6. Colocar el resultado en el _.env_

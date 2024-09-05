
# Watchlist API

Este proyecto utiliza Python para obtener datos utilizando la API de CCL.

## Instrucciones para ejecutar

### 1. Clonar el repositorio


git clone https://github.com/tuusuario/nombre-repositorio.git
cd nombre-repositorio


### 2. Configurar el entorno con `pyenv`

1. Instala `pyenv` y `pyenv-virtualenv` (ver la documentación oficial [aquí](https://github.com/pyenv/pyenv) y [aquí](https://github.com/pyenv/pyenv-virtualenv)).

2. Instala la versión de Python especificada (si no la tienes):

   
   pyenv install 3.x.x  # Reemplaza con la versión adecuada
   

3. Crea y activa el entorno virtual:

   
   pyenv virtualenv 3.x.x watchlist-env
   pyenv local watchlist-env
   

4. Instala las dependencias:

   
   pip install -r requirements.txt
   

### 3. Ejecutar el script


python api_ccl.py


### 4. Añadir un archivo `.gitignore`

Evita subir tu entorno virtual y otros archivos innecesarios a GitHub agregando un archivo `.gitignore` con el siguiente contenido:


watchlist-env/
__pycache__/
*.pyc
*.pyo
.DS_Store


### 5. Subir el proyecto a GitHub

1. Inicia un repositorio en tu carpeta de proyecto:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Crea un nuevo repositorio en GitHub.

3. Conéctalo con tu repositorio local:

   ```bash
   git remote add origin https://github.com/tuusuario/nombre-repositorio.git
   ```

4. Sube tu proyecto:

   ```bash
   git push -u origin master
   ```

### 6. Instrucciones para otros usuarios

Cuando otros clonen tu proyecto, podrán ejecutar estos mismos pasos para configurar el entorno de `pyenv` y ejecutar tu código sin problemas.
```

Este formato es el adecuado para que cualquier persona pueda seguir las instrucciones y ejecutar tu código correctamente usando `pyenv`.
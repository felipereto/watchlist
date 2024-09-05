
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


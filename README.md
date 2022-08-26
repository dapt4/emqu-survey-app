# Correr la applicacion
Para correr la applicacion siga los siguientes pasos

## la aplicacion
### entorno virtual
Para crear el entorno virtual utilice
#### `python -m venv venv`

Para levantar el entorno virtual use
#### `source venv/bin/activate`

### librerias
Para instalar las librerias utilice
#### `pip install -r requirements.txt`

## la Base de datos
### instalación
para iniciar debe instalar MySql

### configuración
Luego debe colocar el usuario, el host, el port, 
la contraseña, y el nombre de la base de datos en 
el archivo `App.py` en la sección:
`#mysql connection`

### crear la base de datos
Luego debe abrir la carpeta `database` y abrir el
archivo `db.sql`, y pegar su contenido en la shell
de MySql

## iniciar la app
Para iniciar la app utilice
#### `python App.py`

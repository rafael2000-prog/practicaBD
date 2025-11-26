# practicaBD

Crear los respectivos archivos

# Para abrir BD de docker

Buscamos los contenedores activos:

docker ps

Abrimos bash de docker:

docker exec -it namedeImagen bash

Instalamos sqlite3:

apt update

apt intall --y sqlite3

Luego abrimos el sqlite:

sqlite3 mensajes.db

SELECT * FROM datos;

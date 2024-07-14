#!/bin/bash

# Paso 1: Crear y levantar el container de PostgreSQL
docker-compose up -d

# Esperar a que el contenedor esté listo
sleep 10

# Paso 2: Crear las tablas en la base de datos
./create_tables.sh

# Paso 3: Popular la base de datos
docker build -t my_app .
docker run --rm --network itba-cloud-data-engineering_default -v .:/app my_app python3 /app/insert_db.py

# Paso 4: Ejecutar consultas
docker run --rm --network itba-cloud-data-engineering_default -v .:/app my_app python3 /app/query_db.py

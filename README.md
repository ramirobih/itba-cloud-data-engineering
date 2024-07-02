# Trabajo Práctico - ITBA Cloud Data Engineering

## Descripción del Dataset
Ver archivo [about.md](about.md).

## Ejercicios

### Ejercicio 1
- Descripción del dataset y preguntas de negocio: [about.md](about.md).

### Ejercicio 2
- Docker Compose para PostgreSQL: [docker-compose.yml](docker-compose.yml).

### Ejercicio 3
- Script de Bash para creación de tablas: [create_tables.sh](create_tables.sh).
- Script SQL para creación de tablas: [create_tables.sql](create_tables.sql).

### Ejercicio 4
- Script de Python para popular la base de datos: [insert_db.py](insert_db.py).
- Dockerfile para el script de Python: [Dockerfile](Dockerfile).

### Ejercicio 5
- Script de Python para consultas: [query_db.py](query_db.py).
- Dockerfile para el script de Python: [Dockerfile](Dockerfile).

### Ejercicio 6
- Script de Bash para ejecución end-to-end: [run_all.sh](run_all.sh)

## Ejecución End-to-End

Para ejecutar todo el proceso end-to-end desde la creación del container, operaciones de DDL, carga de datos y consultas, siga estos pasos:

```bash
./run_all.sh

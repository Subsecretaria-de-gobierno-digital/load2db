load2db

Este repositorio contiene dos scripts de Python para cargar datos desde archivos Excel a bases de datos PostgreSQL:
1. loadDatatoDB_gen.py
Características

Carga datos generales con una columna adicional data_origin
Normaliza archivos Excel
Agrega un valor de origen de datos configurable

Uso
bashCopypython loadDatatoDB_gen.py <archivo_excel> <host> <nombre_bd> <usuario> <contraseña> <nombre_tabla> [--data_origin VALOR_ORIGEN]
Ejemplo
bashCopypython loadDatatoDB_gen.py datos.xlsx localhost mibasedatos miusuario miclave mitabla --data_origin "archivo_enero"
2. loadDatatoDB_specific.py
Características

Carga datos con procesamiento específico
Incluye año de entrada como parámetro
Verifica existencia del archivo de entrada
Normaliza y procesa datos antes de cargar

Uso
bashCopypython loadDatatoDB_specific.py <archivo_excel> <nombre_bd> <host> <usuario> <contraseña> <nombre_tabla> <año>
Ejemplo
bashCopypython loadDatatoDB_specific.py datos2023.xlsx mibasedatos localhost miusuario miclave mitabla 2023
Dependencias
Dependencias Principales

datetime: Manejo de fechas y tiempos
argparse: Procesamiento de argumentos de línea de comandos
os: Verificación de archivos

Dependencias Específicas del Proyecto

load_gen o loadv3: Módulo de carga a base de datos
normalize_gen o normalize: Módulo de normalización de datos
process: Módulo de procesamiento de datos (solo en loadDatatoDB_specific.py)

Instalación

Clonar el repositorio
Instalar dependencias:

bashCopypip install datetime argparse psycopg2 openpyxl
Flujo de Trabajo

Normalización: Convierte el archivo Excel a un formato estandarizado
Procesamiento (específico): Transforma los datos si es necesario
Carga: Inserta los datos en la base de datos PostgreSQL

Consideraciones

Ambos scripts requieren credenciales de base de datos
loadDatatoDB_gen.py es más genérico
loadDatatoDB_specific.py permite mayor personalización

Logging y Seguimiento

Muestra tiempo de ejecución
Imprime mensajes de progreso en consola
No genera archivos de log permanentes

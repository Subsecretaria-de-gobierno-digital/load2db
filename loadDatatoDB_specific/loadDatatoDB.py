import datetime
import argparse as ap
import os

from normalize import normalize
from process import process
from loadv3 import load


def loadDatatoDB(input_file, db_name, host, user, pwd, table_name, input_yr):
    start_time = datetime.datetime.now()

    # Verificar si el archivo existe
    if not os.path.isfile(input_file):
        print(f"Error: El archivo '{input_file}' no existe.")
        return

    print('Normalizing the Excel file...')
    output = normalize(input_file)

    print('Processing the data...')
    processed = process(output)

    print('Loading the data into the database...')
    load(processed, input_yr, db_name, host, user, pwd, table_name)

    print('Done! :)\nTime elapsed: ', datetime.datetime.now() - start_time)


# Configuración de los argumentos
parser = ap.ArgumentParser(description='Load an Excel file into a database')
parser.add_argument('input_file', metavar='input_file', type=str, help='The Excel file to load')
parser.add_argument('db_name', metavar='db_name', type=str, help='The database name')
parser.add_argument('host', metavar='host', type=str, help='The database host')
parser.add_argument('user', metavar='user', type=str, help='The database user')
parser.add_argument('pwd', metavar='pwd', type=str, help='The database password')
parser.add_argument('table_name', metavar='table_name', type=str, help='The table name')
parser.add_argument('input_yr', metavar='input_yr', type=str, help='Intended year from dump')

# Parsear los argumentos
args = parser.parse_args()

# Llamada a la función con todos los argumentos
loadDatatoDB(
    args.input_file,
    args.db_name,
    args.host,
    args.user,
    args.pwd,
    args.table_name,
    args.input_yr
)
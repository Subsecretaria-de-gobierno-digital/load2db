import datetime
import argparse as ap

from load_gen import load
from normalize_gen import normalize 

def loadDatatoDB_gen(input_file, host, db_name, user, password, table_name, data_origin_value="default_value"):
    start_time = datetime.datetime.now()
    print('Normalizing the Excel file...')
    output = normalize(input_file)

    # Añadir la columna 'data_origin' y su valor a cada fila
    output[0].append('data_origin')  # Añadir el nombre de la columna al encabezado
    for row in output[1:]:  # Añadir el valor a cada fila
        row.append(data_origin_value)

    print('Loading the data into the database...')
    load(output, db_name, host, user, password, table_name)

    print('Done! :)\nToday I elapsed: ', datetime.datetime.now() - start_time)


parser = ap.ArgumentParser(description='Load an Excel file into a database')
parser.add_argument('input_file', metavar='input_file', type=str, help='The Excel file to load')
parser.add_argument('host', metavar='host', type=str, help='The database host')
parser.add_argument('db_name', metavar='db_name', type=str, help='The database name')
parser.add_argument('user', metavar='user', type=str, help='The database user')
parser.add_argument('password', metavar='password', type=str, help='The database password')
parser.add_argument('table_name', metavar='table_name', type=str, help='The table name')
parser.add_argument('--data_origin', metavar='data_origin', type=str, default="default_value", help='The value for the data_origin column')
args = parser.parse_args()

loadDatatoDB_gen(args.input_file, args.host, args.db_name, args.user, args.password, args.table_name, args.data_origin)
# try conn pymysql alone 

host_mysql = '192.168.90.183'
port_mysql = 3306
user_mysql = 'consulta-paaas'
password_mysql = 'Paaas.2023'
database_mysql = 'paas'

import sqlalchemy
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine(f'mysql+pymysql://{user_mysql}:{password_mysql}@{host_mysql}:{port_mysql}/{database_mysql}')
conn_mysql = engine.connect()

# Output connection test
print(conn_mysql)

# get detalle_paas
query = """
SELECT * FROM detalle_paas
"""

# pass to powerbi
df = pd.read_sql(query, conn_mysql)
import psycopg2 
from psycopg2 import sql, extras
import time

def load(input_data, host, db_name, user, password, table_name, batch_size=1000):
    cur = None
    conn = None
    try:
        conn = psycopg2.connect(
            dbname = db_name,
            user = user,
            password = password,
            host = host
        )

        cur = conn.cursor()

        columns_to_insert = [col for col in input_data[0]]

        if not columns_to_insert:
            print("No matching columns found. Aborting.")
            return

        # Encontrar los índices de las columnas que quieres insertar
        column_indices_to_insert = [input_data[0].index(col) for col in columns_to_insert]

        # Utilizar esos índices para acceder a los elementos en cada row
        rows_to_insert = [[row[i] for i in column_indices_to_insert] for row in input_data[1:]]

        # Try to create the table if it doesn't exist
        print(f"Creating table '{table_name}' if it doesn't exist...")
        try:
            table_fields = ', '.join([f'{column} TEXT' for column in columns_to_insert])
            cur.execute(sql.SQL(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_fields})'))
            conn.commit()
        except Exception as e:
            print(f"Error during table creation: {e}")
            return

        # Check if the table exists
        cur.execute(sql.SQL("SELECT to_regclass('public.{}')").format(sql.Identifier(table_name)))
        if cur.fetchone()[0] is None:
            print(f"Table '{table_name}' not found after creation attempt. Aborting.")
            return

        # Then insert the new rows
        print("inserting new rows")

        start_time = time.time()  # Start timer

        # Batch insert
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                    sql.Identifier(table_name),
                    sql.SQL(',').join(map(sql.Identifier, columns_to_insert)),
                    sql.SQL(',').join(sql.Placeholder() * len(columns_to_insert))
                )
        print("executing batch insert")
        for i in range(0, len(rows_to_insert), batch_size):
            extras.execute_batch(cur, query, rows_to_insert[i:i+batch_size])

        end_time = time.time()  # End timer

        conn.commit()

        print(f"Inserted {len(rows_to_insert)} rows in {end_time - start_time} seconds.")
    
    finally:
        # This will always run, even if an error occurs above
        if cur:
            cur.close()
        if conn:
            conn.close()

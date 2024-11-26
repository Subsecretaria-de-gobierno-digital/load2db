import psycopg2 
from psycopg2 import sql, extras
import time

def load(input_data, input_yr, db_name, host, user, pwd, table_name):
    conn = psycopg2.connect(
        dbname = db_name,
        user = user,
        password = pwd,
        host = host
    )

    cur = conn.cursor()

    columns = input_data[0]
    columns.append('input_yr')  # Add 'input_yr' as a new column

    # Define columns to be converted to float
    float_columns = ['original', 'ampliacion', 'reduccion', 'modificado', 'pre_comprometido', 'comprometido', 'devengado', 'ejercido', 'pagado']

    table_fields = ', '.join([f'{column} TEXT' for column in columns])

    cur.execute(sql.SQL("SELECT to_regclass('public.{}')").format(sql.Identifier(table_name)))
    if cur.fetchone()[0] is None:
        print(f"The table '{table_name}' does not exist. Creating it now...")
        cur.execute(f"CREATE TABLE {table_name} ({table_fields})")
    else:
        print(f"The table '{table_name}' already exists.")
        # Check if 'input_yr' column exists, if not, add it
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table_name}' and column_name='input_yr';")
        if not cur.fetchone():
            print("The column 'input_yr' does not exist. Adding it now...")
            cur.execute(f"ALTER TABLE {table_name} ADD COLUMN input_yr TEXT;")

    # Check if 'input_yr' matches any existing value
    cur.execute(sql.SQL("SELECT * FROM {} WHERE ejercicio = %s").format(sql.Identifier(table_name)), (input_yr,))
    if cur.fetchone() is not None:
        # If it does, delete it
        print(f"'ejercicio' value '{input_yr}' already exists. Deleting...")
        cur.execute(sql.SQL("DELETE FROM {} WHERE ejercicio = %s").format(sql.Identifier(table_name)), (input_yr,))
        print(f"Deleted 'ejercicio' value '{input_yr}'.")

    # Convert specified columns to float
    rows_to_insert = []
    for row in input_data[1:]:
        new_row = []
        for col, val in zip(columns, row + [input_yr]):
            if col in float_columns:
                try:
                    new_row.append(float(val))
                except ValueError:
                    new_row.append(None)  # Handle conversion error if needed
            else:
                new_row.append(val)
        rows_to_insert.append(new_row)

    start_time = time.time()  # Start timer
    print(f"Inserting new rows for 'ejercicio' value '{input_yr}'...")

    extras.execute_batch(
        cur,
        sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.SQL(',').join(sql.Placeholder() * len(columns))
        ),
        rows_to_insert
    )

    end_time = time.time()  # End timer

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {len(input_data) - 1} rows in {end_time - start_time} seconds.")

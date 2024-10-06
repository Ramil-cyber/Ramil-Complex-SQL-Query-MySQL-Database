import os
import requests
import csv
import sqlite3


def extract_csv(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/nba-draft-2015/historical_projections.csv",
    file_path="nba_draft.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(os.path.join(directory, file_path), "wb") as f:
            f.write(r.content)
    return os.path.join(directory, file_path)


def read_sql(query, **params):
    if query.strip().endswith(".sql"):
        with open(query, "r") as file:
            query = file.read().strip()
    return query.format(**params)


def insert(connection, table_name, values):
    try:
        cursor = connection.cursor()

        _columns = ", ".join(values.keys())
        _values = ", ".join(values.values())

        base_insert_query = read_sql(
            "sql/insert.sql",
            table_name=table_name,
            columns=_columns,
            values=_values,
        )
        print(base_insert_query)
        cursor.execute(base_insert_query)
        connection.commit()

        inserted_id = cursor.lastrowid
        return inserted_id

    except Exception as e:
        print(e)
        return None


def read_by_id(connection, table_name, id, id_col_name="ID"):
    cursor = connection.cursor()

    query = f"SELECT * FROM {table_name} WHERE {id_col_name} = {id} "

    print(query)
    cursor.execute(query)

    data = cursor.fetchone()
    column_names = [description[0] for description in cursor.description]

    result = {"columns": column_names, "data": data}
    return result


def read_all(connection, table_name):
    try:
        cursor = connection.cursor()

        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        result = {"columns": column_names, "data": data}
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def load_csv_to_db(csv_file_path, conn, table_name):
    try:
        cursor = conn.cursor()

        with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)

            columns_to_create_table = ", ".join(
                [f"{col.replace('.', '_').replace(' ', '_')} TEXT" for col in header]
            )

            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_to_create_table})"
            )

            placeholders = ", ".join(["?" for _ in header])
            cursor.execute(f"DELETE FROM {table_name}")

            sql_insert = f"INSERT INTO {table_name} VALUES ({placeholders})"

            for row in csv_reader:
                cursor.execute(sql_insert, row)

        conn.commit()
        return True

    except Exception as e:
        print(e)
        return False


def update(connection, table_name, ids, update_values):
    try:
        cursor = connection.cursor()

        formatted_updates = ", ".join(
            [
                f"{col_name} = '{update_val}'"
                for col_name, update_val in update_values.items()
            ]
        )
        formatted_ids = ", ".join(map(str, ids))

        base_update_query = read_sql(
            "sql/update.sql",
            id=formatted_ids,
            table_name=table_name,
            updates=formatted_updates,
        )

        print(base_update_query)
        cursor.execute(base_update_query)
        connection.commit()
        print(f"{formatted_ids} are updated successfully")

        return True

    except Exception as e:
        print(e)
        return None


def delete(connection, table_name, ids):
    try:
        cursor = connection.cursor()

        formatted_ids = ", ".join(map(str, ids))

        base_delete_query = read_sql(
            "sql/delete.sql", id=formatted_ids, table_name=table_name
        )

        print(base_delete_query)

        cursor.execute(base_delete_query)
        connection.commit()
        print(f"{formatted_ids} are deleted successfully")

        return True

    except Exception as e:
        print(e)
        return None


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)
        connection.commit()
        cursor.close()
        return True

    except Exception as e:
        print(e)
        return False


def connect_db(database_conn):
    conn = sqlite3.connect(f"{database_conn}.db")
    return conn

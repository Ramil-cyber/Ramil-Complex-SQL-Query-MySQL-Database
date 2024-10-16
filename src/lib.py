import requests
import csv
from databricks import sql
import os
from dotenv import load_dotenv

CLUBS_REMOTE_PATH = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/refs/heads/main/data/clubs.csv"
PLAYERS_REMOTE_PATH = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/refs/heads/main/data/players.csv"

load_dotenv()


def read_sql(query, **params):
    if query.strip().endswith(".sql"):
        with open(query, "r") as file:
            query = file.read().strip()
    return query.format(**params)


def extract_csv(
    url,
    file_path,
    directory,
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(os.path.join(directory, file_path), "wb") as f:
            f.write(r.content)
    return os.path.join(directory, file_path)


def load_csv_to_db(csv_file_path, conn, table_name, create_table_sql):
    cursor = None
    try:
        cursor = conn.cursor()
        with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)

            next(csv_reader)

            cursor.execute(read_sql(create_table_sql))

            cursor.execute(f"TRUNCATE TABLE {table_name}")

            sql_insert = f"INSERT INTO {table_name} VALUES "
            rows = []
            for row in csv_reader:
                processed_row = ["Null" if value == "" else value for value in row]
                rows.append(processed_row)

            values_str = ", ".join(
                [f"({', '.join([repr(v) for v in row])})" for row in rows]
            )
            full_sql = sql_insert + values_str.replace("'Null'", "Null")
            # print(full_sql)
            cursor.execute(full_sql)

        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()


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


def fetchall_result(connection, query, query_params):
    cursor = None
    try:
        cursor = connection.cursor()
        full_exec_query = read_sql(query, **query_params)
        print(f"Query to be executed - \n{full_exec_query}")
        cursor.execute(full_exec_query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Exception occurred - {e}")
        return []
    finally:
        if cursor:
            cursor.close()


def connect_db(database_conn):

    conn = sql.connect(**database_conn)
    return conn


if __name__ == "__main__":
    server_host_name = os.getenv("SERVER_HOSTNAME")
    http_path = os.getenv("HTTP_PATH")
    access_token = os.getenv("ACCESS_TOKEN")

    clubs_path = extract_csv(
        url=CLUBS_REMOTE_PATH, file_path="clubs.csv", directory="data"
    )

    players_path = extract_csv(
        url=PLAYERS_REMOTE_PATH, file_path="players.csv", directory="data"
    )

    connection = connect_db(
        database_conn={
            "server_hostname": server_host_name,
            "http_path": http_path,
            "access_token": access_token,
        },
    )

    load_csv_to_db(
        clubs_path,
        connection,
        table_name="rm564_football_clubs",
        create_table_sql="sql/create_sql_clubs.sql",
    )

    load_csv_to_db(
        players_path,
        connection,
        table_name="rm564_football_clubs_players",
        create_table_sql="sql/create_sql_players.sql",
    )

    connection.close()

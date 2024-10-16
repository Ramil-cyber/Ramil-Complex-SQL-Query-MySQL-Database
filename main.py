from src.lib import (
    connect_db,
    extract_csv,
    load_csv_to_db,
    fetchall_result,
)
import os

CLUBS_REMOTE_PATH = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/refs/heads/main/data/clubs.csv"
PLAYERS_REMOTE_PATH = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Complex-SQL-Query-MySQL-Database/refs/heads/main/data/players.csv"

server_host_name = os.getenv("SERVER_HOSTNAME")
http_path = os.getenv("HTTP_PATH")
access_token = os.getenv("ACCESS_TOKEN")


def extract_csv_to_databricks():

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

    return True


def analytical_queries():
    connection = connect_db(
        database_conn={
            "server_hostname": server_host_name,
            "http_path": http_path,
            "access_token": access_token,
        },
    )

    res = fetchall_result(connection, query="sql/query1.sql", query_params={})
    print(res)
    connection.close()
    return True


if __name__ == "__main__":
    extract_csv_to_databricks()
    analytical_queries()

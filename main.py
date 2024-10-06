from src.lib import (
    extract_csv,
    read_sql,
    insert,
    read_by_id,
    load_csv_to_db,
    update,
    delete,
    execute_query,
    connect_db,
)

CSV_FILE_PATH = "data/nba_draft.csv"
TABLE_NAME = "NbaDraft"
TABLE_NAME_AFTER_TRANSFORMATION = "NbaDraftTransformed"


def elt_perform():

    connection = connect_db("data/database")
    file_path = extract_csv()
    load_csv_to_db(file_path, connection, "NbaDraft")

    execute_query(
        connection, query=f"DROP TABLE IF EXISTS {TABLE_NAME_AFTER_TRANSFORMATION}"
    )
    # Create a transformed table
    execute_query(
        connection,
        query=read_sql("sql/transform.sql", table_name=TABLE_NAME_AFTER_TRANSFORMATION),
    )

    return True


def crud_operations():
    status = False

    connection = connect_db("data/database")
    # Read operation
    random_id_data = read_by_id(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, id="'karl-anthony-towns'"
    )
    print(f"Retrieved result - {random_id_data}")
    # Create (Insert) operation
    inserted_row_id = insert(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, {"ID": "'ramil-mammadov1'"}
    )
    inserted_row_id2 = insert(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, {"ID": "'ramil-mammadov2'"}
    )
    print(f"Inserted Row Ids:{inserted_row_id}, {inserted_row_id2}")
    # Update operation
    status = update(
        connection,
        table_name=TABLE_NAME_AFTER_TRANSFORMATION,
        ids=["'ramil-mammadov1'"],
        update_values={"Position": "SF", "Player": "Ramil Mammadov"},
    )
    updated_id_data = read_by_id(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, id="'ramil-mammadov1'"
    )
    print(updated_id_data)
    # Delete operation
    status = delete(
        connection,
        table_name=TABLE_NAME_AFTER_TRANSFORMATION,
        ids=["'ramil-mammadov2'"],
    )

    return status


def analytical_queries():
    connection = connect_db("data/database")
    cursor = connection.cursor()
    cursor.execute(read_sql(query="sql/query1.sql"))
    print(read_sql(query="sql/query1.sql"))
    result = cursor.fetchall()
    print(result)
    print("-" * 60)
    cursor.execute(read_sql(query="sql/query2.sql"))
    print(read_sql(query="sql/query2.sql"))
    result2 = cursor.fetchall()
    print(result2)
    cursor.close()

    return True


if __name__ == "__main__":
    elt_perform()
    crud_operations()
    analytical_queries()

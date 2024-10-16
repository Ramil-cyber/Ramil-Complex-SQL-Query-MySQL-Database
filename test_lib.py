import pytest
import os
from src.lib import connect_db, execute_query, fetchall_result


@pytest.fixture
def databricks_connection():
    """Fixture to establish a real Databricks connection and close it after use."""

    # Load environment variables
    server_host_name = os.getenv("SERVER_HOSTNAME")
    http_path = os.getenv("HTTP_PATH")
    access_token = os.getenv("ACCESS_TOKEN")

    # Establish the connection using your connect_db function
    conn = connect_db(
        database_conn={
            "server_hostname": server_host_name,
            "http_path": http_path,
            "access_token": access_token,
        }
    )

    # Yield the connection to the tests
    yield conn

    # Close the connection after use
    conn.close()


def test_connect_db_databricks(databricks_connection):
    """Test connecting to Databricks using a real connection."""
    assert databricks_connection is not None


def test_execute_query_databricks(databricks_connection):
    """Test executing a query on Databricks using a real connection."""
    query = "SELECT 1"

    result = execute_query(databricks_connection, query)

    assert result is True


def test_fetchall_result_databricks(databricks_connection):
    """Test fetching results from a real query on Databricks."""
    query = (
        "SELECT * FROM ids706_data_engineering.default.rm564_football_clubs_players "
    )
    query_params = {}

    result = fetchall_result(databricks_connection, query, query_params)

    assert len(result) != 0

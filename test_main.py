import sqlite3
import pytest
from src.lib import (
    read_all,
    insert,
    read_by_id,
    update,
    delete,
    connect_db,
)
from main import elt_perform, crud_operations, analytical_queries


# Fixture to create an in-memory SQLite database
@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


# Test insert
def test_insert(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")

    values = {"id": "1", "name": "'John'"}
    inserted_id = insert(connection, "test_table", values)

    assert inserted_id == 1

    cursor.execute("SELECT * FROM test_table WHERE id = 1")
    row = cursor.fetchone()
    assert row == (1, "John")


# Test read_by_id
def test_read_by_id(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John')")

    result = read_by_id(connection, "test_table", 1)

    assert result["data"] == (1, "John")
    assert result["columns"] == ["id", "name"]


# Test read_all
def test_read_all(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John')")

    result = read_all(connection, "test_table")

    assert result["data"] == [(1, "John")]
    assert result["columns"] == ["id", "name"]


# Test update
def test_update(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John')")

    update_values = {"name": "Jane"}
    success = update(connection, "test_table", [1], update_values)

    assert success is True

    cursor.execute("SELECT name FROM test_table WHERE id = 1")
    updated_name = cursor.fetchone()[0]
    assert updated_name == "Jane"


# Test delete
def test_delete(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John')")

    success = delete(connection, "test_table", [1])
    assert success is True

    cursor.execute("SELECT * FROM test_table WHERE id = 1")
    result = cursor.fetchone()
    assert result is None


# Test connect_db
def test_connect_db():
    conn = connect_db("data/database")
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


# Test connect_db
def test_main_db():
    assert elt_perform()
    assert crud_operations()
    assert analytical_queries()

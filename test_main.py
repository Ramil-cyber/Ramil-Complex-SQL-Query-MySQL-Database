from main import extract_csv_to_databricks, analytical_queries


def test_main():
    res1 = extract_csv_to_databricks()
    res2 = analytical_queries()

    assert res1
    assert res2

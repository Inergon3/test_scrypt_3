import pytest

from app.data import Data


@pytest.fixture
def test_csv_file(tmp_path):
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(
        "name,brand,price,rating\niphone 15 pro,apple,999,4.9\ngalaxy s23 ultra,samsung,1199,4.8\n"
    )
    return test_file


@pytest.fixture
def data():
    return Data()

def test_return_data(data, test_csv_file):
    result = data.return_data(test_csv_file, "price>1000", "price=avg")
    assert result == {"avg": 1199.0}
import pytest

from app.reader import Reader


@pytest.fixture
def test_csv_file(tmp_path):
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(
        "name,brand,price,rating\niphone 15 pro,apple,999,4.9\ngalaxy s23 ultra,samsung,1199,4.8\n"
    )
    return test_file


@pytest.fixture
def reader():
    return Reader()


def test_read(reader, test_csv_file):
    data = reader.read([test_csv_file])
    assert data == [
        [
            ["name", "brand", "price", "rating"],
            ["iphone 15 pro", "apple", "999", "4.9"],
            ["galaxy s23 ultra", "samsung", "1199", "4.8"],
        ]
    ]


def test_return_dict(reader, test_csv_file):
    data = reader.return_dict([test_csv_file])
    assert data == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        },
    ]

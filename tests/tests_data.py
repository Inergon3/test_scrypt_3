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
def data_obj():
    return Data()


def test_return_data(data_obj, test_csv_file):
    result_more_avg = data_obj.return_data([test_csv_file], "price>1000", "price=avg")
    result_less_min = data_obj.return_data([test_csv_file], "price<1000", "price=min")
    result_all = data_obj.return_data([test_csv_file])
    result_more = data_obj.return_data([test_csv_file], "price>1000")
    result_max = data_obj.return_data([test_csv_file], aggregate="price=max")
    assert result_more_avg == [{"avg": 1199.0}]
    assert result_less_min == [{"min": 999}]
    assert result_all == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        },
    ]
    assert result_more == [
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        }
    ]
    assert result_max == [{"max": 1199}]

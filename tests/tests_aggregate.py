import pytest
from app.aggregate import Aggregate


@pytest.fixture
def test_dicts():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        },
    ]


@pytest.fixture
def agregate():
    return Aggregate()


def test_min(agregate, test_dicts):
    data = agregate.min_price(test_dicts)
    assert data == [{"min": 999}]


def test_max(agregate, test_dicts):
    data = agregate.max_price(test_dicts)
    assert data == [{"max": 1199}]


def test_avg(agregate, test_dicts):
    data = agregate.avg_price(test_dicts)
    assert data == [{"avg": 1099.0}]


def test_return_data(agregate, test_dicts):
    data_min = agregate.return_data(test_dicts, "min")
    data_max = agregate.return_data(test_dicts, "max")
    data_avg = agregate.return_data(test_dicts, "avg")
    assert data_min == [{"min": 999}]
    assert data_max == [{"max": 1199}]
    assert data_avg == [{"avg": 1099.0}]


def test_return_data_error(agregate, test_dicts):
    with pytest.raises(ValueError):
        agregate.return_data(test_dicts, "<min")
    with pytest.raises(ValueError):
        agregate.return_data(test_dicts, ">max")
    with pytest.raises(ValueError):
        agregate.return_data(test_dicts, "=avg")

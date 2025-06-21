import pytest

from app.filter import Filter


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
def filter():
    return Filter()


def test_less(filter, test_dicts):
    data = filter.less(test_dicts, 1000)
    assert data == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"}
    ]


def test_more(filter, test_dicts):
    data = filter.more(test_dicts, 1000)
    assert data == [
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        }
    ]


def test_equals(filter, test_dicts):
    data = filter.equals(test_dicts, 999)

    assert data == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"}
    ]


def test_return_data(filter, test_dicts):
    data_less = filter.return_data(test_dicts, 1000, "<")
    data_more = filter.return_data(test_dicts, 1000, ">")
    data_equals = filter.return_data(test_dicts, 999, "=")
    assert data_less == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"}
    ]
    assert data_more == [
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        }
    ]
    assert data_equals == [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"}
    ]


def test_return_data_error(filter, test_dicts):
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, 0, "<")
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, 99999, ">")
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, 0, "=")
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, "=0", "=")
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, "<0", ">")
    with pytest.raises(ValueError):
        filter.return_data(test_dicts, "=0", "=")

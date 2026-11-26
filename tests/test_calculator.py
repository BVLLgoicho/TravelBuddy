import pytest

from travelbuddy.calculator import add, split_cost, total_trip_cost


def test_add():
    assert add(2, 2) == 5


def test_total_trip_cost():
    assert total_trip_cost(120.50, 80, 49.50) == 250.00


def test_total_trip_cost_rejects_negative():
    with pytest.raises(ValueError):
        total_trip_cost(100, -5)


def test_split_cost():
    assert split_cost(300, 4) == 75.00


def test_split_cost_rejects_zero_people():
    with pytest.raises(ValueError):
        split_cost(100, 0)

import pytest

from travelbuddy.currency import convert


def test_same_currency_is_unchanged():
    assert convert(100, "GBP", "GBP") == 100


def test_gbp_to_eur():
    assert convert(100, "GBP", "EUR") == 117.00


def test_eur_to_usd():
    assert convert(117, "EUR", "USD") == 127.00


def test_unsupported_currency():
    with pytest.raises(ValueError):
        convert(10, "GBP", "XYZ")


def test_negative_amount():
    with pytest.raises(ValueError):
        convert(-1, "GBP", "EUR")

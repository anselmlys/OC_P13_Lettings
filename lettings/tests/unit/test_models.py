import pytest


@pytest.mark.django_db
def test_letting_model(letting):
    expected_value = 'somewhere'

    assert str(letting) == expected_value


@pytest.mark.django_db
def test_address_model(address):
    expected_value = '1 over the rainbow'

    assert str(address) == expected_value

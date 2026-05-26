import pytest

from lettings.models import Letting, Address


@pytest.fixture
def address():
    return Address.objects.create(number=1,
                                  street='over the rainbow',
                                  city='somewhere',
                                  state='HI',
                                  zip_code=96795,
                                  country_iso_code='USA')


@pytest.fixture
def letting(address):
    return Letting.objects.create(title='somewhere', address=address)

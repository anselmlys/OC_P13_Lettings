import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_lettings_index_view(letting):
    client = Client()

    path = reverse('lettings:lettings_index')
    response = client.get(path)
    content = response.content.decode()
    expected_fixed_content = 'Lettings'

    assert response.status_code == 200
    assert letting.title in content
    assert expected_fixed_content in content


@pytest.mark.django_db
def test_letting_info_view(letting):
    client = Client()

    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert letting.title in content
    assert '<p>1 over the rainbow</p>' in content

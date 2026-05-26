import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_profiles_index_view(profile):
    client = Client()
    path = reverse('profiles:profiles_index')
    response = client.get(path)
    content = response.content.decode()
    expected_fixed_content = 'Profiles'

    assert response.status_code == 200
    assert expected_fixed_content in content
    assert profile.user.username in content


@pytest.mark.django_db
def test_profile_view(profile):
    client = Client()
    path = reverse('profiles:profile', kwargs={'username': profile.user.username})
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert profile.user.username in content

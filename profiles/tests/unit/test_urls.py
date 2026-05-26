from django.urls import reverse, resolve

from profiles import views


def test_profiles_index_url():
    path = reverse('profiles:profiles_index')

    assert path == '/profiles/'
    assert resolve(path).func == views.profiles_index


def test_profile_info_url():
    path = reverse('profiles:profile', kwargs={'username': 'test'})

    assert path == '/profiles/test/'
    assert resolve(path).func == views.profile

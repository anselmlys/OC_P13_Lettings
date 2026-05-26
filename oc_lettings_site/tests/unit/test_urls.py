from django.urls import reverse, resolve

from oc_lettings_site import views


def test_index_url():
    path = reverse('index')

    assert path == '/'
    assert resolve(path).func == views.index


def test_lettings_urls_are_included():
    path = '/lettings/'

    assert resolve(path).namespace == 'lettings'


def test_profiles_urls_are_included():
    path = '/profiles/'

    assert resolve(path).namespace == 'profiles'

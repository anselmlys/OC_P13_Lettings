from django.urls import reverse, resolve

from lettings import views


def test_lettings_index_url():
    path = reverse('lettings:lettings_index')

    assert path == '/lettings/'
    assert resolve(path).func == views.lettings_index


def test_letting_info_url():
    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    assert path == '/lettings/1/'
    assert resolve(path).func == views.letting

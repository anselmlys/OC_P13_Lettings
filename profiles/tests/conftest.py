import pytest

from django.contrib.auth import get_user_model
from profiles.models import Profile


User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create(username='janedoe', password='test')


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, favorite_city='london')

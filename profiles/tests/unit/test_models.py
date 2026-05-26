import pytest

from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_profile_model(profile):
    assert str(profile) == 'janedoe'

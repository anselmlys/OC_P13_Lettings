'''Handle views for the profiles application.'''

import logging
from django.http import Http404
from django.shortcuts import render

from profiles.models import Profile


logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):
    '''
    Display the list of all profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered profiles index page.
    '''

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}

    return render(request, 'profiles/profiles_index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    '''
    Display the detail page for a user profile.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): The username associated with the profile.

    Returns:
        HttpResponse: The rendered profile detail page.
    '''

    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning('Profile not found for username=%s', username)
        raise Http404('Profile not found')

    context = {'profile': profile}

    return render(request, 'profiles/profile.html', context)

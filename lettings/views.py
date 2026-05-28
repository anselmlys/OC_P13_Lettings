'''Handle views for the lettings application.'''

import logging
from django.http import Http404
from django.shortcuts import render

from lettings.models import Letting


logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
def lettings_index(request):
    '''
    Display the list of all available lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered lettings index page.
    '''

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/lettings_index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue,
# dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    '''
    Display the detail page for a specific letting.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The unique identifier of the letting.

    Returns:
        HttpResponse: The rendered letting detail page.
    '''

    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning('Letting not found for letting_id=%s', letting_id)
        raise Http404('Letting not found')

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

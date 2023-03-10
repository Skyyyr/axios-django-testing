import json
import os
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


def home(request):
    """
    This is our way of loading a custom HTML file instead of using the default django page
    :param request:
    :return:
    """
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)


@api_view(['POST', 'GET'])
def test_route(request):
    results = 'INVALID'

    if request.method == 'POST':
        results = 'POST'

    elif request.method == 'GET':
        results = 'GET'

    return JsonResponse({'valid': results})


@api_view(['GET'])
def display_data(request):
    """
    This is a basic example of making a request to the backend from the frontend and sending data as an object
    :param request:
    :return: an object with some data sent from the backend to the front end
    """

    data_object = {
        'data_set_one': "This is the value of 'data_set_one'",
        'data_set_two': "This is the value of 'data_set_two'",
    }

    return JsonResponse(data_object)


@api_view(['GET'])
def local_data(request):
    """
    This is an example of loading a local file then sending it across html as an object

    :param request:
    :return: an object with a list of data that was loaded from a local file
    """
    data = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../external_data.json")

    with open(path) as loc_dat:
        reader = json.load(loc_dat)
        for row in reader:
            data.append(row)

    return JsonResponse({'loaded_data': data})


@api_view(['POST'])
def telephone(request):
    # As you see here we just send back the data that was sent to us
    return JsonResponse(request.data)

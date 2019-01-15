import json

import requests
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from bot.django_api import get_url


# Create your views here.
def index(request):
    return HttpResponse('Hello World!')


def alarms(request):
    open_id = request.GET.get('open_id')
    uuid = request.GET.get('uuid')
    url = get_url(open_id, uuid)
    response = requests.get(url=url)
    result = json.loads(response.content.decode())
    template = loader.get_template('alarm.html')
    context = {'alarm_list': result}
    return HttpResponse(template.render(context, request))

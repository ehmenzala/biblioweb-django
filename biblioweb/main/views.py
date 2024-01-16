from django.http import HttpResponse
from django.template import loader


def index(request) -> HttpResponse:
    index_template = loader.get_template('index.html')
    return HttpResponse(index_template.render({}, request))

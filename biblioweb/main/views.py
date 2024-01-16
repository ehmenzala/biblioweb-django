from django.http import HttpResponse, HttpRequest
from django.template import loader


def index(request: HttpRequest) -> HttpResponse:
    index_template = loader.get_template('index.html')
    return HttpResponse(index_template.render({}, request))

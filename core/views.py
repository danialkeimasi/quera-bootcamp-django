from django.shortcuts import HttpResponse
from django.http import HttpRequest


def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the core index.")

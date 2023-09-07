from uuid import UUID

from django.http import HttpRequest
from django.shortcuts import HttpResponse


def index_view(request: HttpRequest):
    return HttpResponse(f"Hello, world. You're at the {request.path_info}")


def hello_view(request: HttpRequest, name: str):
    return HttpResponse(f"Hello, {name.title()}. You're at the {request.path_info}")


def sum_view(request: HttpRequest, a: int, b: int):
    return HttpResponse(f"{a} + {b} = {a + b}")


def slug_view(request: HttpRequest, slug: str):
    return HttpResponse(f"Slug: {slug}")


def uuid_view(request: HttpRequest, uuid: UUID):
    return HttpResponse(f"UUID: {uuid}")


def drink(request: HttpRequest, drink: str):
    return HttpResponse(f"Drink: {drink}")

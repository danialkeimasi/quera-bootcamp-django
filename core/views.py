from uuid import UUID

from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string


def index_view(request: HttpRequest):
    response_as_string = render_to_string("core/index.html", request=request)
    return HttpResponse(response_as_string)


def hello_view(request: HttpRequest, name: str):
    reserved_names = [
        "quera",
        "bootcamp",
        "college",
        "contest",
    ]
    return render(
        request,
        "core/hello.html",
        context={
            "name": name,
            "reserved_names": reserved_names,
            "is_quera": name.lower() in reserved_names,
        },
    )


def sum_view(request: HttpRequest, a: int, b: int):
    return HttpResponse(f"{a} + {b} = {a + b}")


def slug_view(request: HttpRequest, slug: str):
    return HttpResponse(f"Slug: {slug}")


def uuid_view(request: HttpRequest, uuid: UUID):
    return HttpResponse(f"UUID: {uuid}")


def drink(request: HttpRequest, drink: str):
    return HttpResponse(f"Drink: {drink}")

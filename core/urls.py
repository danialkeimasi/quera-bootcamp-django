from django.urls import path, re_path
from django.urls.converters import register_converter

from . import converters, views

register_converter(converters.DrinkConverter, "drink")

urlpatterns = [
    path("", views.index_view, name="index"),
    path("hello/<str:name>", views.hello_view, name="hello"),
    path("sum/<int:a>/<int:b>", views.sum_view, name="sum"),
    path("slug/<slug:slug>", views.slug_view, name="slug"),
    path("uuid/<uuid:uuid>", views.uuid_view, name="uuid"),
    re_path(r"^drink/(?P<drink>coke|water|dough)/$", views.drink, name="land"),
    path("custom_drink/<drink:drink>/", views.drink, name="drink"),
]

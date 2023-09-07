from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("hello/<str:name>", views.hello_view, name="hello"),
    path("sum/<int:a>/<int:b>", views.sum_view, name="sum"),
    path("slug/<slug:slug>", views.slug_view, name="slug"),
    path("uuid/<uuid:uuid>", views.uuid_view, name="uuid"),
]

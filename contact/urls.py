from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [
    path("", views.contact_view, name="contact"),
    path("csat/", views.csat_view, name="csat"),
]

from django.http import HttpRequest
from django.shortcuts import render

from .forms import ContactForm, CSATForm


def contact_view(request: HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact/success.html")
    else:
        form = ContactForm(initial={"name": "Initial Name"})
    return render(request, "contact/form.html", context={"form": form})


def csat_view(request: HttpRequest):
    if request.method == "POST":
        form = CSATForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact/success.html")
    else:
        form = CSATForm()
    return render(request, "contact/form.html", context={"form": form})

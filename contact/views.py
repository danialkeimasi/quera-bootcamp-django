from django.http import HttpRequest
from django.shortcuts import render

from .forms import ContactForm


def contact_view(request: HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact/success.html")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", context={"form": form})

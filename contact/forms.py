from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 30, "cols": 80, "placeholder": "Your message here."}),
        }
        labels = {
            "name": "Your Beautiful Name",
        }
        help_texts = {
            "name": ("Before you ask, yes, I think you are beautiful."),
        }
        error_messages = {
            "name": {
                "min_length": "Your name is too short. It must be at least 3 characters long.",
            },
        }

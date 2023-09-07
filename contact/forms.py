from django import forms
from django.core.validators import MinLengthValidator

from .models import CSAT, Contact


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


class CSATForm(forms.Form):
    rating = forms.IntegerField(label="How would you rate your experience?", min_value=1, max_value=5)
    comment = forms.CharField(
        label="Do you have any comments?",
        widget=forms.Textarea(attrs={"rows": 30, "cols": 80, "placeholder": "Your message here."}),
        required=False,
        validators=[
            MinLengthValidator(10, message="Comment must be at least 10 characters long."),
        ],
    )

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating == 1:
            raise forms.ValidationError("Nah man, you can't rate 1 star.")
        return rating

    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")
        comment = cleaned_data.get("comment")
        if rating and comment:
            if rating < 3 and len(comment) < 20:
                raise forms.ValidationError("Please provide more details when rating less than 3 stars.")
        return cleaned_data

    def save(self):
        rating = self.cleaned_data["rating"]
        comment = self.cleaned_data["comment"]
        CSAT.objects.create(rating=rating, comment=comment)

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.db.models import Q


def validate_name(value: str):
    # https://docs.djangoproject.com/en/4.2/ref/validators/#writing-validators

    if value.lower() in ["danial keimasi", "daishogun"]:
        raise ValidationError(f"{value}, go back to work.")


class Contact(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(email="") | ~Q(phone_number=""),
                name="email_or_phone_number",
                violation_error_message="Either email or phone number should be provided.",
            )
        ]

    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(r"^[a-zA-Z]*$", "Only characters are allowed."),
            MinLengthValidator(3),
            validate_name,
        ],
    )
    email = models.EmailField(blank=True)
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        validators=[
            RegexValidator(r"^09[0-9]+$", "Phone number should be 11 digits and start with 09."),
        ],
    )
    message = models.TextField(
        validators=[
            MinLengthValidator(10),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    def clean(self) -> None:
        # use this method to validate fields that depend on each other

        if self.name.lower() == "bagher" and self.email == "":
            raise ValidationError("Bagher is not allowed.")

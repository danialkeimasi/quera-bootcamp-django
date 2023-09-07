# Generated by Django 4.2.5 on 2023-09-07 21:48

import django.core.validators
from django.db import migrations, models

import contact.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator("^[a-zA-Z]*$", "Only characters are allowed."),
                            django.core.validators.MinLengthValidator(3),
                            contact.models.validate_name,
                        ],
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^09[0-9]+$", "Phone number should be 11 digits and start with 09."
                            )
                        ],
                    ),
                ),
                ("message", models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("resolved", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddConstraint(
            model_name="contact",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("email", ""), _negated=True),
                    models.Q(("phone_number", ""), _negated=True),
                    _connector="OR",
                ),
                name="email_or_phone_number",
                violation_error_message="Either email or phone number should be provided.",
            ),
        ),
    ]

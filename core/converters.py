from django.urls.converters import StringConverter


class DrinkConverter(StringConverter):
    regex = r"coke|water|dough"

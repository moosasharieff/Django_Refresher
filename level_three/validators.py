from django.core.validators import ValidationError

def check_for_m(value):
    """ Raise a ValidationError if the first letter does not start with 'M' """
    if value[0].lower() != "m":
        raise ValidationError(message="The name should start with letter : 'M'")
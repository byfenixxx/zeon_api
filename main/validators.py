import os
from django.core.exceptions import ValidationError


def validate_file_extensions(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
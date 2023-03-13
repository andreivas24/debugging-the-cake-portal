from django.core.exceptions import ValidationError


def validate_tag_type(tag_type):

    if not isinstance(tag_type, str) or not tag_type.isalpha():
        raise ValidationError("'tag_type' must be a string")

    # if not tag_type.islower() or not tag_type.isupper() or not tag_type[0].isupper():
    #     raise ValidationError("'tag_type' does not respect a specific pattern")

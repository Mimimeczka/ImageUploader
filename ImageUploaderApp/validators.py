from django.core.exceptions import ValidationError


def check_account_type(type_from_url, user_account_type):

    if type_from_url == 'small':
        int_type_from_url = 1
    elif type_from_url == 'medium':
        int_type_from_url = 2
    elif type_from_url == 'original':
        int_type_from_url = 3
    else:
        raise ValidationError('Wrong url type')

    if user_account_type < int_type_from_url:
        raise ValidationError('Wrong account type')

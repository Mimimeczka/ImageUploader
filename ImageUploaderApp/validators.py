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


def check_image_type(image_name):
    image_name = image_name.lower()
    if not image_name.endswith('.jpg') or image_name.endswith('.png'):
        raise ValidationError('Wrong file extension')


def check_image_owner(user_id, image):
    user_id_from_image = image.user_id.pk
    if user_id != user_id_from_image:
        raise ValidationError('Wrong image owner')
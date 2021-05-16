from django.test import TestCase
from .validators import check_account_type, check_image_type
from django.core.exceptions import ValidationError


class ValidatorsTest(TestCase):

    def test_check_account_type(self):
        with self.assertRaises(ValidationError):
            check_account_type('medium', 1)

    def test_check_account_type_wrong_type(self):
        with self.assertRaises(ValidationError):
            check_account_type('test', 1)

    def test_check_image_type(self):
        with self.assertRaises(ValidationError):
            check_image_type('test.pdf')


from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from datetime import date, datetime

def val_pat_id(value):
    if not str(value).isalnum():
        raise ValidationError(
            _('Error! Patient ID cannot contain special characters!'),
            params={'value': value},
        )

def valid_dob(value):
    today = datetime.now()
    min = datetime(2000, 1, 1, 1, 0, 0)
    dob = datetime.strptime(str(value), '%Y-%m-%d')
    if dob > today or dob < min:
        raise ValidationError(
            _('Please enter a valid date of birth'),
            params={'value': value},
        )
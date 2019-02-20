from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(regex = r'^\+\d{8,15}$', message = _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


class PhoneNumberField(models.CharField):
	default_validators = [phone_regex]
	description = _("Phone number")

	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 20)
		super().__init__(*args, **kwargs)

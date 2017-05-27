from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

try:
	UNIQUE = settings.USER_PHONE_NUMBER_UNIQUE
except AttributeError:
	UNIQUE = False


def normalize_phone_number(phone_number):
	return phone_number.strip().replace(' ', '').replace('-', '')


phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


class PhoneNumberField(models.CharField):
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 20
		kwargs['validators'] = [phone_regex]
		super().__init__(*args, **kwargs)


class PhoneNumberMixin(models.Model):
	class Meta:
		abstract = True

	phone_number = PhoneNumberField(_('phone number'), blank=True, unique=UNIQUE)

	def clean(self):
		super().clean()
		self.phone_number = normalize_phone_number(self.phone_number)

	class Admin:
		fieldsets = (
			(None, dict(fields = ('phone_number',))),
		)
		list_display = ('phone_number',)
		search_fields = ('phone_number',)

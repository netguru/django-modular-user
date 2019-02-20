from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_modular_user.fields import PhoneNumberField

try:
	UNIQUE = settings.USER_PHONE_NUMBER_UNIQUE
except AttributeError:
	UNIQUE = False


def normalize_phone_number(phone_number):
	"""
	Normalize the phone number by removing all spaces and dashes.
	"""
	if phone_number is None:
		return None
	return phone_number.strip().replace(' ', '').replace('-', '')


class PhoneNumberMixin(models.Model):
	class Meta:
		abstract = True

	phone_number = PhoneNumberField(_('phone number'), blank = True, null = True, unique = UNIQUE)

	def clean(self):
		super().clean()
		self.phone_number = normalize_phone_number(self.phone_number)

	class Admin:
		fieldsets = ((None, dict(fields = ('phone_number',))),)
		list_display = ('phone_number',)
		search_fields = ('phone_number',)

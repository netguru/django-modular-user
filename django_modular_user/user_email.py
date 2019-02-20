from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

try:
	UNIQUE = settings.USER_EMAIL_UNIQUE
except AttributeError:
	UNIQUE = False


def normalize_email(email):
	"""
	Normalize the email address by lowercasing the domain part of it.
	"""
	if email is None:
		return None
	try:
		email_name, domain_part = email.strip().rsplit('@', 1)
	except ValueError:
		pass
	else:
		email = '@'.join([email_name, domain_part.lower()])
	return email


class EmailMixin(models.Model):
	class Meta:
		abstract = True

	email = models.EmailField(_('email address'), blank = True, null = True, unique = UNIQUE)

	def clean(self):
		super().clean()
		self.email = normalize_email(self.email)

	class Admin:
		fieldsets = ((None, dict(fields = ('email',))),)
		list_display = ('email',)
		search_fields = ('email',)

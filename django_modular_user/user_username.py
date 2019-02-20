import unicodedata

from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def normalize_username(username):
	return unicodedata.normalize('NFKC', username) if username else username


class UsernameMixin(models.Model):
	class Meta:
		abstract = True

	if getattr(settings, 'USERNAME_FIELD', None) is None:
		USERNAME_FIELD = 'username'

	_username_validator = UnicodeUsernameValidator()

	username = models.CharField(
		_('username'),
		max_length = 150,
		unique = True,
		help_text = _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		validators = [_username_validator],
		error_messages = {
			'unique': _("A user with that username already exists."),
		},
	)

	def clean(self):
		super().clean()
		self.username = normalize_username(self.username)

	class Admin:
		fieldsets = ((None, dict(fields = ('username',))),)
		list_display = ('username',)
		search_fields = ('username',)
		ordering = ('username',)

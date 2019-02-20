from django.contrib.auth import password_validation
from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.db import models
from django.utils.crypto import get_random_string, salted_hmac
from django.utils.translation import gettext_lazy as _


def make_random_password(self, length = 10, allowed_chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
	"""
	Generate a random password with the given length and given
	allowed_chars. The default value of allowed_chars does not have "I" or
	"O" or letters and digits that look similar -- just to avoid confusion.
	"""
	return get_random_string(length, allowed_chars)


class PasswordMixin(models.Model):
	class Meta:
		abstract = True

	password = models.CharField(_('password'), max_length = 128)

	class Admin:
		fieldsets = ((None, dict(fields = ('password',))),)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Stores the raw password if set_password() is called so that it can
		# be passed to password_changed() after the model is saved.
		self._password = None

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self._password is not None:
			password_validation.password_changed(self._password, self)
			self._password = None

	def set_password(self, raw_password):
		self.password = make_password(raw_password)
		self._password = raw_password

	def check_password(self, raw_password):
		"""
		Return a boolean of whether the raw_password was correct. Handles
		hashing formats behind the scenes.
		"""

		def setter(raw_password):
			self.set_password(raw_password)
			# Password hash upgrades shouldn't be considered password changes.
			self._password = None
			self.save(update_fields = ["password"])

		return check_password(raw_password, self.password, setter)

	def set_unusable_password(self):
		# Set a value that will never be a valid hash
		self.password = make_password(None)

	def has_usable_password(self):
		return is_password_usable(self.password)

	def get_session_auth_hash(self):
		"""
		Return an HMAC of the password field.
		"""
		key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
		return salted_hmac(key_salt, self.password).hexdigest()

import uuid

from django.db import models


class UserManager(models.Manager):
	use_in_migrations = True

	def get_by_natural_key(self, username):
		return self.get(**{self.model.USERNAME_FIELD: username})

	def _create_user(self, password, **data):
		user = self.model(**data)
		user.clean()
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, **data):
		return self._create_user(**data)

	def create_superuser(self, **data):
		if self.model.is_staff:
			data.setdefault('is_staff', True)
			if data['is_staff'] is not True:
				raise ValueError('Superuser must have is_staff=True.')

		if self.model.is_superuser:
			data.setdefault('is_superuser', True)
			if data['is_superuser'] is not True:
				raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(**data)


class AbstractBaseUser(models.Model):
	objects = UserManager()

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	is_anonymous = False
	is_authenticated = True
	is_active = True
	is_staff = False

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'id'

	class Meta:
		abstract = True

	def get_username(self):
		"Return the identifying username for this User"
		return getattr(self, self.USERNAME_FIELD)

	def __str__(self):
		return str(self.get_username())

	def natural_key(self):
		return (self.get_username(),)

	def get_full_name(self): # TODO remove in Django 2.0
		return ''

	def get_short_name(self): # TODO remove in Django 2.0
		return ''

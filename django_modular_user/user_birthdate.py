from django.db import models
from django.utils.translation import gettext_lazy as _


class BirthdateMixin(models.Model):
	class Meta:
		abstract = True

	birthdate = models.DateField(_('birthdate'), blank = True, null = True)

	class Admin:
		fieldsets = ((_('Profile'), dict(fields = ('birthdate',))),)

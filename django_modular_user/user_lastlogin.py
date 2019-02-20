from django.db import models
from django.utils.translation import gettext_lazy as _


class LastLoginMixin(models.Model):
	class Meta:
		abstract = True

	last_login = models.DateTimeField(_('last login'), blank = True, null = True)

	class Admin:
		fieldsets = ((_('Important dates'), dict(fields = ('last_login',))),)

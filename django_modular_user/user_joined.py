from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class JoinedMixin(models.Model):
	class Meta:
		abstract = True

	date_joined = models.DateTimeField(_('date joined'), default = timezone.now)

	class Admin:
		fieldsets = ((_('Important dates'), dict(fields = ('date_joined',))),)

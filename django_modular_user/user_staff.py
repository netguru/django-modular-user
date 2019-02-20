from django.db import models
from django.utils.translation import gettext_lazy as _


class StaffMixin(models.Model):
	class Meta:
		abstract = True

	is_staff = models.BooleanField(
		_('staff status'),
		default = False,
		help_text = _('Designates whether the user can log into this admin site.'),
	)

	class Admin:
		list_display = ('is_staff',)
		list_filter = ('is_staff',)
		fieldsets = ((_('Permissions'), dict(fields = ('is_staff',))),)

from django.db import models
from django.utils.translation import gettext_lazy as _


class ActiveMixin(models.Model):
	class Meta:
		abstract = True

	is_active = models.BooleanField(
		_('active'),
		default = True,
		help_text = _('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
	)

	class Admin:
		list_display = ('is_active',)
		list_filter = ('is_active',)
		fieldsets = ((_('Permissions'), dict(fields = ('is_active',))),)

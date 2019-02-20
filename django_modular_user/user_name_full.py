from django.db import models
from django.utils.translation import gettext_lazy as _


class FullNameMixin(models.Model):
	class Meta:
		abstract = True

	name = models.CharField(_('full name'), max_length = 200, blank = True, null = True)
	nickname = models.CharField(_('nickname'), max_length = 200, blank = True, null = True)

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.nickname

	class Admin:
		list_display = ('nickname', 'name')
		search_fields = ('nickname', 'name')
		fieldsets = ((_('Profile'), dict(fields = ('name', 'nickname'))),)

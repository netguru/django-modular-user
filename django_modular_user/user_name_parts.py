from django.db import models
from django.utils.translation import gettext_lazy as _


class NamePartsMixin(models.Model):
	class Meta:
		abstract = True

	given_name = models.CharField(_('given name'), max_length = 200, blank = True, null = True)
	middle_name = models.CharField(_('middle name'), max_length = 200, blank = True, null = True)
	family_name = models.CharField(_('family name'), max_length = 200, blank = True, null = True)

	@property
	def nickname(self):
		return self.given_name

	@property
	def name(self):
		if self.given_name is None and self.middle_name is None and self.family_name is None:
			return None
		# Split/join this way because the name fields can contain spaces.
		return ' '.join('{} {} {}'.format(self.given_name or '', self.middle_name or '', self.family_name or '').split())

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.nickname

	class Admin:
		list_display = ('nickname', 'name')
		search_fields = ('given_name', 'middle_name', 'family_name')
		fieldsets = ((_('Profile'), dict(fields = ('given_name', 'middle_name', 'family_name'))),)

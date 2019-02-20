from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressMixin(models.Model):
	class Meta:
		abstract = True

	address_formatted = models.TextField(_("formatted address"), blank = True, null = True)
	address_street = models.CharField(_("street"), max_length = 200, blank = True, null = True)
	address_locality = models.CharField(_("locality"), max_length = 200, blank = True, null = True)
	address_region = models.CharField(_("region"), max_length = 200, blank = True, null = True)
	address_postal_code = models.CharField(_("postal code"), max_length = 50, blank = True, null = True)
	address_country = models.CharField(_("country"), max_length = 50, blank = True, null = True)

	@property
	def address(self):
		return {
			'formatted': self.address_formatted,
			'street_address': self.address_street,
			'locality': self.address_locality,
			'region': self.address_region,
			'postal_code': self.address_postal_code,
			'country': self.address_country,
		}

	@address.setter
	def address(self, v):
		self.address_formatted = v.get('formatted')
		self.address_street = v.get('street_address')
		self.address_locality = v.get('locality')
		self.address_region = v.get('region')
		self.address_postal_code = v.get('postal_code')
		self.address_country = v.get('country')

		if self.address_formatted is None and self.address_country is not None:
			parts = [self.address_street, self.address_locality, self.address_region, self.address_postal_code, self.address_country.upper()]
			parts = [p for p in parts if p is not None]
			self.address_formatted = '\n'.join(parts)

	class Admin:
		fieldsets = ((_("Address"), dict(fields = ('address_formatted', 'address_street', 'address_locality', 'address_region', 'address_postal_code', 'address_country'))),)

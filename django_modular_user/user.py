from importlib import import_module

from django.apps import apps
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .user_active import ActiveMixin
from .user_address import AddressMixin
from .user_base import AbstractBaseUser
from .user_birthdate import BirthdateMixin
from .user_email import EmailMixin
from .user_joined import JoinedMixin
from .user_lastlogin import LastLoginMixin
from .user_name_full import FullNameMixin
from .user_name_parts import NamePartsMixin
from .user_password import PasswordMixin
from .user_permissions import PermissionsMixin
from .user_phone_number import PhoneNumberMixin
from .user_staff import StaffMixin
from .user_username import UsernameMixin

__all__ = ['AbstractBaseUser', 'UsernameMixin', 'EmailMixin', 'PhoneNumberMixin', 'FullNameMixin', 'NamePartsMixin', 'PasswordMixin', 'ActiveMixin', 'StaffMixin', 'PermissionsMixin', 'LastLoginMixin', 'JoinedMixin', 'BirthdateMixin', 'AddressMixin']

try:
	CORE_MODULES = settings.USER_CORE_MODULES
except AttributeError:
	CORE_MODULES = [
		'django_modular_user.user:AbstractBaseUser',
		'django_modular_user.user:UsernameMixin',
		'django_modular_user.user:EmailMixin',
		'django_modular_user.user:PhoneNumberMixin',
		'django_modular_user.user:FullNameMixin',
		'django_modular_user.user:PasswordMixin',
		'django_modular_user.user:ActiveMixin',
		'django_modular_user.user:StaffMixin',
		'django_modular_user.user:PermissionsMixin',
		'django_modular_user.user:LastLoginMixin',
		'django_modular_user.user:JoinedMixin',
		'django_modular_user.user:AddressMixin',
	]

bases = []

for module in CORE_MODULES:
	try:
		mod, cls = module.split(':', 1)
	except ValueError:
		mod = module
		cls = 'UserMixin'

	bases.append(getattr(import_module(mod), cls))

for app in apps.get_app_configs():
	try:
		bases.append(import_module(app.name + '.user').UserMixin)
	except ImportError as e:
		pass


class AbstractUser(*reversed(bases)):
	class Meta:
		abstract = True
		verbose_name = _('user')
		verbose_name_plural = _('users')

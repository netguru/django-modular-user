from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.translation import gettext_lazy as _


# A few helper functions for common logic between User and AnonymousUser.
def _user_get_all_permissions(user, obj):
	permissions = set()
	for backend in auth.get_backends():
		if hasattr(backend, "get_all_permissions"):
			permissions.update(backend.get_all_permissions(user, obj))
	return permissions


def _user_has_perm(user, perm, obj):
	"""
	A backend can raise `PermissionDenied` to short-circuit permission checking.
	"""
	for backend in auth.get_backends():
		if not hasattr(backend, 'has_perm'):
			continue
		try:
			if backend.has_perm(user, perm, obj):
				return True
		except PermissionDenied:
			return False
	return False


def _user_has_module_perms(user, app_label):
	"""
	A backend can raise `PermissionDenied` to short-circuit permission checking.
	"""
	for backend in auth.get_backends():
		if not hasattr(backend, 'has_module_perms'):
			continue
		try:
			if backend.has_module_perms(user, app_label):
				return True
		except PermissionDenied:
			return False
	return False


class PermissionsMixin(models.Model):
	"""
	Add the fields and methods necessary to support the Group and Permission
	models using the ModelBackend.
	"""
	is_superuser = models.BooleanField(
		_('superuser status'),
		default = False,
		help_text = _('Designates that this user has all permissions without explicitly assigning them.'),
	)
	groups = models.ManyToManyField(
		'auth.Group',
		verbose_name = _('groups'),
		blank = True,
		help_text = _('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
		related_name = "user_set",
		related_query_name = "user",
	)
	user_permissions = models.ManyToManyField(
		'auth.Permission',
		verbose_name = _('user permissions'),
		blank = True,
		help_text = _('Specific permissions for this user.'),
		related_name = "user_set",
		related_query_name = "user",
	)

	class Meta:
		abstract = True

	class Admin:
		list_display = ('is_superuser',)
		list_filter = ('is_superuser', 'groups')
		filter_horizontal = ('groups', 'user_permissions')
		fieldsets = ((_('Permissions'), dict(fields = ('is_superuser', 'groups', 'user_permissions'))),)

	def get_group_permissions(self, obj = None):
		"""
		Return a list of permission strings that this user has through their
		groups. Query all available auth backends. If an object is passed in,
		return only permissions matching this object.
		"""
		permissions = set()
		for backend in auth.get_backends():
			if hasattr(backend, "get_group_permissions"):
				permissions.update(backend.get_group_permissions(self, obj))
		return permissions

	def get_all_permissions(self, obj = None):
		return _user_get_all_permissions(self, obj)

	def has_perm(self, perm, obj = None):
		"""
		Return True if the user has the specified permission. Query all
		available auth backends, but return immediately if any backend returns
		True. Thus, a user who has permission from a single auth backend is
		assumed to have permission in general. If an object is provided, check
		permissions for that object.
		"""
		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True

		# Otherwise we need to check the backends.
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj = None):
		"""
		Return True if the user has each of the specified permissions. If
		object is passed, check if the user has all required perms for it.
		"""
		return all(self.has_perm(perm, obj) for perm in perm_list)

	def has_module_perms(self, app_label):
		"""
		Return True if the user has any permissions in the given app label.
		Use simlar logic as has_perm(), above.
		"""
		# Active superusers have all permissions.
		if self.is_active and self.is_superuser:
			return True

		return _user_has_module_perms(self, app_label)

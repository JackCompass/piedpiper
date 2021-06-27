from django.apps import AppConfig


class PiperuserConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'piperuser'

	def ready(self):
		import piperuser.signals
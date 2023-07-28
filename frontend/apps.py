import glob
from pathlib import Path
import importlib
import sys
from django.apps import AppConfig


class FrontendConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "frontend"

    def ready(self):
        """Load every python file under 'frontend/src' to register them as a django-component
        """
        for path in glob.iglob("frontend/src/**/*.py", recursive=True):
            import_file(path)


def import_file(path):
    MODULE_PATH = path
    MODULE_NAME = Path(path).stem
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

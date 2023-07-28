"""
Template loader that loads templates from each Django app's "components" directory.

Copied from https://github.com/EmilStenstrom/django-components

This is required because django-components expects each component to be in
a folder named 'component' either within an application folder, or within
the root.

We changed the 'component_dir' as 'src/components' so django-components can
render HTML files within the 'src/components' directory.
"""

from pathlib import Path

from django.conf import settings
from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.template.utils import get_app_template_dirs


class DjangoComponentsLoader(FilesystemLoader):
    def get_dirs(self):
        component_dir = "src/components"
        directories = list(get_app_template_dirs(component_dir))

        if settings.SETTINGS_MODULE:
            settings_path = Path(*settings.SETTINGS_MODULE.split("."))

            path = (settings_path / ".." / component_dir).resolve()
            if path.is_dir():
                directories.append(path)

            path = (settings_path / ".." / ".." / component_dir).resolve()
            if path.is_dir():
                directories.append(path)

        return directories

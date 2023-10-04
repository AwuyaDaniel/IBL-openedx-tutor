"""
IBL_openedx_app Django application initialization.
"""

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import (
    PluginURLs,
    PluginSettings,
    ProjectType,
    SettingsType,
)
# from openedx.core.djangoapps.plugins.constants import PluginURLs

class IblOpenedxAppConfig(AppConfig):
    """
    Configuration for the IBL_openedx_app Django application.
    """
    default_auto_field = "django.db.models.BigAutoField"

    name = 'tutoribl_openedx_tutor'
    plugin_app = {
        # mcdaniel oct-2021
        # this is how you inject a python list of urls into lms.urls.py
        #
        # The three dict attributes literally equate to the following
        # lines of code being injected into edx-platform/lms/urls.py:
        #
        # import openedx_plugin_cms.urls.py
        # url(r"^openedx_plugin/cms", include((urls, "openedx_plugin_cms"), namespace="openedx_plugin_cms")),
        PluginURLs.CONFIG: {
            ProjectType.CMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^tutoribl_openedx_tutor/lms/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        # mcdaniel oct-2021
        # this is how you inject settings into lms.envs.common.py and lms.envs.production.py
        # relative_path == a python module in this repo
        #
        # This dict causes all constants defined in this settings/common.py and settings.production.py
        # to be injected into edx-platform/lms/envs/common.py and edx-platform/lms/envs/production.py
        # Refer to settings/common.py and settings.production.py for example implementation patterns.
        # PluginSettings.CONFIG: {
        #     ProjectType.CMS: {
        #         SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: "settings.production"},
        #         SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
        #     }
        # },
    }

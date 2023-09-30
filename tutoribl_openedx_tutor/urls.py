"""
URLs for IBL_openedx_app.
"""
from django.urls import path
from .views import UserGreetings

patched_urlpatterns = [
    path('/greeting', UserGreetings.as_view(), name='greeting'),
]

# Monkey patch the project's urls.py to add the new URLs
# from lms import urls as project_urls
#
# project_urls.urlpatterns += patched_urlpatterns

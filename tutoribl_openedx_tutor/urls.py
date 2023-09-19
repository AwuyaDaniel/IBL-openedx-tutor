"""
URLs for IBL_openedx_app.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

# urlpatterns = [
#     # TODO: Fill in URL patterns and views here.
#     # re_path(r'', TemplateView.as_view(template_name="IBL_openedx_app/base.html")),
# ]

from django.urls import path
from .views import UserGreetings

urlpatterns = [
    path('/greeting', UserGreetings.as_view(), name='greeting'),
]

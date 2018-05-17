from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from pyhawks.apps.core.views import letsencrypt1, letsencrypt2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('.well-known/acme-challenge/ABp6xBPOOdxK4W8OMKiqLntaxZDxxnAoFIYHUNWnPag', letsencrypt1),
    path('.well-known/acme-challenge/QvxfKr8WTh3PGyxDxTec_zSAHhiQchDSWeie23rMgwI', letsencrypt2),
    path('admin/', admin.site.urls),
]

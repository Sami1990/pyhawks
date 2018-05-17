from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from pyhawks.apps.core.views import letsencrypt1, letsencrypt2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('.well-known/acme-challenge/q6hRTs6iOXlgVgI94gUxh1qTLMuhf7SMm7Zo59Lwwzg', letsencrypt1),
    path('.well-known/acme-challenge/1qMP4xHZjjjQuwiU8Bjz0-bnsdmsv7VSHPmG8r3ij04', letsencrypt2),
    path('admin/', admin.site.urls),
]

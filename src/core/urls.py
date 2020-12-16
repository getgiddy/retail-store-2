from django.urls.conf import path
from core import views


urlpatterns = [
    path('', views.home, name='home'),
]

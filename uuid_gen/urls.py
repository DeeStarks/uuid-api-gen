from django.urls import path
from . import views

namespace = 'uuid_endpoint'

urlpatterns = [
    path('', views.uuid, name='create_fetch'),
]
from django.urls import path
from .views import DigiView


urlpatterns = [
    path('', DigiView, name='digi-view'),
]

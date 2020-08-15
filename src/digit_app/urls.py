from django.urls import path
from .views import DigitAppHomeView

urlpatterns = [
    path('', DigitAppHomeView, name='digit-app-home-view'),
]

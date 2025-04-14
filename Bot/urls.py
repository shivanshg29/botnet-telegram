from django.urls import path
from .views import *

urlpatterns=[
    path('',home),
    path('bot/',telegram_webhook),
]
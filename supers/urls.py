from django.urls import re_path
from . import views


urlpatterns = [
    path('supers/', views.supers_list),
]
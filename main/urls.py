from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.variable_info_view, name='main'),
]

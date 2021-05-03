from django.urls import path
from . import views

urlpatterns = [
    # ex: /dashboard/
    path('', views.index, name='index'),
]

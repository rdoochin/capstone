from django.urls import path

from . import views

urlpatterns = [
    # ex: /dashboard/
    path('', views.index, name='index'),
    # ex: /dashboard/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /dashboard/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /dashboard/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

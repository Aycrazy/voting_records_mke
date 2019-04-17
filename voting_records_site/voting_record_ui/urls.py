from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:file_number>/', views.detail, name = 'detail'),
    path('<int:file_number>/results/', views.results, name = 'results'),
    path('<int:file_number>/votes/', views.votes, name='votes')
]

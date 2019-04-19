from django.urls import path

from . import views

app_name = 'voting_record_ui'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:file_number>/', views.detail, name='detail'),
    # path('<int:file_number>/results/',
    #      views.results, name='results'),
    path('<int:file_number>/votes/', views.get_votes, name='votes')
]


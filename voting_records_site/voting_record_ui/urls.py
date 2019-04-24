from django.urls import path

from . import views

app_name = 'voting_record_ui'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail', views.detail, name='detail'),
    # path('<int:file_number>/results/',
    #      views.results, name='results'),
    path('search', views.search_votes, name='search'),
    path('<int:file_number>/votes/', views.get_votes, name='votes')
]


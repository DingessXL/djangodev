from django.conf.urls import url
from . import views

app_name = 'trivia'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^manage/', views.CreateQuestionView.as_view(success_url="manage"), name='manage'),
    url(r'^edit/', views.CreateQuestionView.as_view(success_url="edit"), name='edit'),
    url(r'^new_cat/', views.CreateCategoryView.as_view(success_url="New Category"), name='New Category'),
    url(r'^base/', views.last_ten_questions, name='base'),
]

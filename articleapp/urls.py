from django.urls import path
from articleapp.views import ArticleCreateView

app_name = 'articleapp'

urlpatterns = [
    path('create/', ArticleCreateView.as_view() , name='create'),
    # path('list/', TemplateView(template_name='articleapp/list.html'), name='list'),
]
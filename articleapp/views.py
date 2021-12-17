from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 임시
    template_name = 'articleapp/create.html'

# class ArticleDetailView(DetailView):
#     model =
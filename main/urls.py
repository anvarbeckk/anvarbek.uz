from django.urls import path
from .views import HomeView, BlogView, ArticleView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', ArticleView.as_view(), name='article'),
    path('about/', AboutView.as_view(), name='about')
]
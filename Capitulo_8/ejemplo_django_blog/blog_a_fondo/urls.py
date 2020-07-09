from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.PostListView.as_view(), name='post_main'),
    path('', views.CategoryListView.as_view(), name='category_main'),
]